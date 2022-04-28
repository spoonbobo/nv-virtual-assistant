#!/bin/bash
source config_chatbot.sh
temp_result_folder_path=$RIVA_MOUNTED_RESULTS_DIR/text_classification/text_classification_0
temp_local_result_folder_path=$LOCAL_RESULT_DIR/text_classification/text_classification_0

# 1. Check count for version
version_count="$(ls "$LOCAL_RESULT_DIR/text_classification" | wc -l )"

if [[ $version_count -ge 1 ]];
then
        temp_result_folder_path=$RIVA_MOUNTED_RESULTS_DIR/text_classification/text_classification_$version_count
        temp_local_result_folder_path=$LOCAL_RESULT_DIR/text_classification/text_classification_$version_count
fi

# 2. TAO Toolkit: text classification task
echo "The TAO-trained model will be stored at $temp_local_result_folder_path (docker: $temp_result_folder_path)"

tao text_classification train \
        -e $RIVA_MOUNTED_SPECS_DIR/text_classification/train.yaml \
        -g $GPUS \
        -k $ENCRYPTION_KEY \
        -r $temp_result_folder_path \
        training_ds.file_path=$RIVA_MOUNTED_DATA_DIR/$DOMAIN/text_classification/train.tsv \
        validation_ds.file_path=$RIVA_MOUNTED_DATA_DIR/$DOMAIN/text_classification/val.tsv \
        model.class_labels.class_labels_file=$RIVA_MOUNTED_DATA_DIR/$DOMAIN/text_classification/labels.csv \
        model.dataset.num_classes=$NUM_CLASSES \
        trainer.max_epochs=$NUM_EPOCH

# 3. TAO Toolkit: export text classification model to RIVA format
tao text_classification export \
        -e "$RIVA_MOUNTED_SPECS_DIR/text_classification/export.yaml" \
        -g $GPUS \
        -m $temp_result_folder_path/checkpoints/trained-model.tlt \
        -k $ENCRYPTION_KEY \
        -r $temp_result_folder_path/export_riva \
        export_format=RIVA

# 4. TAO Toolkit: export RIVA format model to rmir
docker run --gpus all --rm -v $temp_local_result_folder_path/export_riva:/servicemaker-dev \
        -v $RIVA_REPO:/riva-repo --entrypoint="/bin/bash" \
        $RIVA_SERVICE_MAKER /riva-repo/build_rmir_nlp_tc.sh
