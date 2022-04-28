def dgx_resp(query):
    if query == "greet":
        return ["Hi! "]

    elif query == "goodbye":
        return ["Goodbye! "]

    elif query == "affirm":
        return ["Sure:) "]

    elif query == "deny":
        return [":( "]

    elif query == "thank":
        return ["You welcome! "]

    elif query == "ask_dgx_system_verify_install":
        return [
            "Before using NVSM, you can verify the installation to make sure all the services are present.",
            " ",
            "Verifying DSHM Serivces",
            "Systemctl status nvsm-env-dshm",
            "sudo systemctl status nvsm-storage-dshm",
            "sudo systemctl status nvsm-sys-dshm",
            "sudo systemctl status nvsm-env-dshm",
            " ",
            "Verifying NVSM APIs Services:",
            "sudo systemctl status nvsm-apis-plugin-memory",
            "sudo systemctl status -all nvsm-apis*",
        ]

    elif query == "ask_dgx_system_cli":
        return [
            'NVIDIA DGX-2 servers running DGX OS version 4.0.1 or later should come with NVSM pre-installed. NVSM CLI communicates with the privileged NVSM API server, so NVSM CLI requires superuser privileges to run. All examples given in this guide are prefixed with the "sudo" command', ' ',

            'use NVSM CLI interactively:',
            'sudo nvsm',
            'nvsm-> show fans',
            '(to terminate, type exit)', ' ',

            ',use NVSM CLI non-interactively:',
            ',sudo nvsm show fans', ' ',

            'guide for using man page:',
            'https://docs.nvidia.com/datacenter/nvsm/19.06/nvsm-user-guide/index.html#topic_3_3'
        ]

    elif query == "ask_dgx_system_health":
        return ['The most basic functionality of NVSM CLI is examination of system state. NVSM CLI provides a "show" command for this purpose. Because NVSM CLI is modeled after the SMASH CLP, the output of the NVSM CLI "show" command should be familiar to users of BMC command line interfaces.', ' ',

                'Common commands:', ' ',

                'Show health:',
                'sudo nvsm show health -> display overall system health', ' ',

                'Dump health:',
                'sudo nvsm dump health -> generates a health report file', ' ',

                'Show storage:',
                'sudo nvsm show storage -> display all storage-related information',
                'sudo nvsm show drives -> display the storage drives',
                'sudo nvsm show volumes -> display the storage volumns', ' ',

                'Show GPUs:',
                'sudo nvsm show gpus -> display your gpus', ' ',

                'Show processors:',
                'sudo nvsm show processors -> display information for all CPUs in system', ' ',

                'Show memory:',
                'sudo nvsm show memory -> displays information for all installed DIMMs',
                'sudo nvsm show dimms -> alias of "show memory"', ' ',

                'Show fans and temperature',
                'sudo nvsm show fans',
                'sudo nvsm show temperatures',
                'sudo nvsm show temps -> alias of "show temperatures"', ' ',

                'Show power supplies:',
                'sudo nvsm show psus -> alias of power supplies']

    elif query == "ask_dgx_system_configuration":
        return ["NVSM provides a DSHM service that monitors the state of the DGX system. NVSM CLI can be used to interact with the DSHM system monitoring service via the NVSM API server.", " ",

                "configure email alerts:",
                "click https://docs.nvidia.com/datacenter/nvsm/19.06/nvsm-user-guide/index.html#topic_3_5_1", " ",

                "understand different system monitoring policies:",
                "click https://docs.nvidia.com/datacenter/nvsm/19.06/nvsm-user-guide/index.html#topic_3_5_2"]

    elif query == "ask_dgx_system_security":
        return ["NVSM APIs are served using the HTTPS protocol. HTTPS requires the NVSM API server to possess a public-private key pair as well as a certificate that it presents to connecting clients. The certificate also needs to be signed by a certificate authority (CA) using the private key of that CA.", " ",

                "You'll need the followings to configure NVSM Security:",
                "1. X.509 certificate for the NVSM REST server (/pki/node1.crt)",
                "2. Private key file corresponding to the above certificate (/pki/node1.key)",
                "3. The certificate of the CA who issued the above certificate (/pki/ca.crt)", " ",

                "To configure NVSM Security:",
                "1. Edit the NVSM configuration file to use the paths and filenames of your certificate files and key file. Edit the ca_cert, https_cert, and https_priv_key configuration parameters to specify the path and filenames that NVSM shall use. The following use the example path and filenames.", " ",

                "2. Restart the NVSM service",
                "sudo systemctl restart nvsm"]

    elif query == "ask_dgx_system_nvsm_apis":
        return ['You can call NVSM APIs from your application using command shell, python, or browser. Refer to NVSM API Reference (https://docs.nvidia.com/datacenter/nvsm/) for more details., ' ' ',

                'First, you should get authorization to call NVSM APIs following the below syntax:',
                'ssh -t <user>@<DGX Node IP> "sudo nvsm_apis -gentoken <days of validity>"',
                'For example:',
                'ssh -t dgxadmin@dc1_dgx2_node1 "sudo nvsm_apis -gentoken 2"', ' ',

                'Then, you may call APIs through command line, python, or a browser. Refer to https://docs.nvidia.com/datacenter/nvsm/19.06/nvsm-user-guide/index.html#nvsm-api-calling-specifics for more details.']

    elif query == "ask_dgx_a100_gpu":
        return ["Qty 8 NVIDIA A100 GPUs",
                "Third-generation NVLinks"]

    elif query == "ask_dgx_a100_overview":
        return ["The NVIDIA DGX™ A100 system is the universal system purpose-built for all AI infrastructure and workloads, from analytics to training to inference. ",
                "The system is built on eight NVIDIA A100 Tensor Core GPUs."]

    elif query == "ask_dgx_a100_options":
        return ["There are two options of the NVIDIA DGX A100 system:",
                "the NVIDIA DGX A100 640GB system and the NVIDIA DGX A100 320GB system."]

    elif query == "ask_dgx_a100_nvswitch":
        return ["The NVSwitch component of Qty of 6 for NVIDIA DGX A100 640GB/ 320GB Systems.",
                "2nd generation of NVSwitch on DGXA100 is 2x faster than the 1st generation (600 GB/s GPU-to-GPU bandwidth)"]

    elif query == "ask_dgx_a100_networking":
        return ["Networking component for NVIDIA DGX A100 640GB System:",
                "Qty 10 (Factory ship config)",
                "Mellanox ConnectX-6 VPI HDR InfiniBand/200 Gb/s Ethernet", " ",

                "Networking component for NVIDIA DGX A100 320GB System:",
                "Qty 9 (Factory ship config)",
                "Mellanox ConnectX-6 VPIHDR IB/200 Gb/s",
                "(Optional Add-on: Second dualport 200 Gb/s Ethernet)", " ",

                "Network (Cluster) card:",
                "Mellanox ConnectX-6 Single Port VPI",
                "InfiniBand (default): HDR, HDR100, EDR",
                "Ethernet: 200GbE, 100GbE, 50GbE, 40GbE, 25GbE, and 10GbE", " ",

                "Network (Storage) card:",
                "Mellanox ConnectX-6 Dual Port VPI",
                "Ethernet (default): 200GbE, 100GbE, 50GbE, 40GbE, 25GbE, and,10GbEInfiniBand: HDR, HDR100, EDR"]

    elif query == "ask_dgx_a100_cpu":
        return ["DGX A100 has 2 AMD Rome (2x AMD EPYC 7742 CPU w/64 cores)"]

    elif query == "ask_dgx_a100_system_memory":
        return ["System Memory component for NVIDIA DGX A100 640GB System: 2 TB (Factory ship config)", " ",

                "System Memory component for NVIDIA DGX A100 320GB System:",
                "1 TB (Factory ship config)",
                "(Optional Add-on: 1 TB to get 2 TB max.)", " ",

                "System Memory (DIMM): 1 TB per 16 DIMMs"]

    elif query == "ask_dgx_a100_storage":
        return ["Drives specifications for NVIDIA DGX A100 640GB System:",
                "30 TB (Factory ship config)",
                "U.2 NVMe Drives", " ",

                "Drives specifications for NVIDIA DGX A100 320GB System:",
                "15 TB (Factory ship config)",
                "U.2 NVMe Drives",
                "(Optional Add-on: 15 TB to get 30 TB max.)", " ",

                "Storege (OS): 1.92 TB NVMe M.2 SSD (ea) in RAID 1 array",
                "Storage (Data Cache): 3.84 TB NVMe U.2 SED (ea) in RAID 0 array"]

    elif query == "ask_dgx_a100_band_system_management":
        return ["BMC (out-of-band system management):"
                "1 GbE RJ45 interface"
                "Supports IPMI, SNMP, KVM, and Web UI",

                "In-band system management:"
                "1 GbE RJ45 interface"]

    elif query == "ask_dgx_a100_power_supply":
        return ["The DGX A100 system contains six power supplies with balanced distribution of the power load:", " ",

                "Input -> 200-240 volts AC, 6.5 kW max."
                "Specification -> 3000 W @ 200-240 V, 16 A, 50-60 Hz", " ",

                "Support for N+N Redundancy: Support for N+N Redundancy:", " ",

                "The DGX A100 includes six power supply units (PSU) configured for 3+3 redundancy. If three PSUs fail, the system will continue to operate at full power with the remaining three PSUs."]

    elif query == "ask_dgx_a100_mechanical_spec":
        return ['Mechanical specifications for DGX A100:', ' ',

                'Form Factor: 6U Rackmount',
                'Height: 10.4" (264 mm)',
                'Width: 19" (482.3 mm) max',
                'Depth: 35.3" (897.1 mm) max',
                'System Weight: 271.5 lbs (123.16 kg) max']

    elif query == "ask_dgx_a100_environ_spec":
        return ["Environmental specifications for DGX A100:", " ",

                "Operating Temperature: 5 C to 30 C (41 F to 86 F)",
                "Relative Humidity: 20% to 80% non-condensing",
                "Airflow: 840 CFM @ 80% fan PWM",
                "Heat Output: 22,179 BTU/hr"]

    elif query == "ask_dgx_a100_network_hw":
        return ["The DGX A100 system is not shipped with network cables or adaptors. You will need to purchase supported cables or adaptors for your network.",
                "The ConnectX-6 firmware determines which cables and adaptors are supported. For a list of cables and adaptors compatible with the Mellanox ConnectX-6 VPI cards installed in the DGX A100 system,", " ",

                "1 Visit the Mellanox Firmware Release page (https://docs.mellanox.com/category/adapterfw%20).", " ",

                "2. From the left navigation menu, select the ConnectX model and corresponding firmware included in the DGX A100.", " ",

                "3. Select Firmware Compatible Products."]

    elif query == "ask_dgx_a100_os_software":
        return ["The DGX A100 system comes pre-installed with a DGX software stack incorporating:",
                "-> An Ubuntu server distribution with supporting packages", " ",

                "-> The following system management and monitoring software",
                "• NVIDIA System Management (NVSM)",
                "Provides active health monitoring and system alerts for NVIDIA DGX nodes in a data center. It also provides simple commands for checking the health of the DGX A100 system from the command line.", " ",

                "• Data Center GPU Management (DCGM)",
                "This software enables node-wide administration of GPUs and can be used for cluster and data-center level management.", " ",

                "-> DGX A100 system support packages", " ",

                "-> The NVIDIA GPU driver", " ",

                "-> Docker Engine", " ",

                "-> NVIDIA Container Toolkit", " ",

                "-> Mellanox OpenFabrics Enterprise Distribution for Linux (MOFED)", " ",

                "-> Mellanox Software Tools (MST)", " ",

                "-> cachefilesd (daemon for managing cache data storage)"]

    elif query == "ask_dgx_a100_documentation":
        return ["-> MIG User Guide (https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html)",
                "The new Multi-Instance GPU (MIG) feature allows the NVIDIA A100 GPU to be securely partitioned into up to seven separate GPU Instances for CUDA applications.", " ",

                "-> NGC Container Registry for DGX (https://docs.nvidia.com/ngc/ngc-private-registry-user-guide/index.html)",
                "How to access the NGC container registry for using containerized deep learning GPUaccelerated applications on your DGX A100 system.", " ",

                "-> NVSM Software User Guide (https://docs.nvidia.com/datacenter/nvsm/latest/nvsm-user-guide/index.html)",
                "Contains instructions for using the NVIDIA System Management software.", " ",

                "-> DCGM Software User Guide (https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-user-guide/index.html)",
                "Contains instructions for using the Data Center GPU Manager software."]

    elif query == "ask_dgx_a100_customer_support":
        return ["Contact NVIDIA Enterprise Support for assistance in reporting, troubleshooting, or diagnosing problems with your DGX A100 system. Also contact NVIDIA Enterprise Support for assistance in moving the DGX A100 system.", " ",

                "-> For contracted Enterprise Support questions, you can send an email:", " ",
                "enterprisesupport@nvidia.com", " ",

                "-> For additional details on how to obtain support, visit the NVIDIA Enterprise Support web site (https://www.nvidia.com/en-us/support/enterprise/ )", " ",

                "Our support team can help collect appropriate information about your issue and involve internal resources as needed."]

    elif query == "ask_dgx_a100_significant_leap":
        return ["Technology improvements include:"
                "-> World's largest 7 nm GPU, with 54B transistors and 40 GB HBM2.",
                "-> Third generation Tensor Cores: Faster, new precisions, and easier to use.",
                "-> Compared to NVIDIA® V100 GPU floating point 32 (FP32), speed improvements of:",
                "-> 20X artificial intelligence (AI) training — TensorFloat-32 (TF32)",
                "-> 20X AI inference — Integer 8 (INT8)",
                "-> 2.5X high performance computing (HPC) — floating point 64 (FP64)",
                "-> New Sparsity acceleration: 2X acceleration on sparse AI models",
                "-> New Multi-instance GPU (MIG)"
                "-> Third generation NVIDIA NVLink interconnect technology and NVIDIA NVSwitch on-chip memory fabric"]

    elif query == "ask_dgx_a100_fulfil_workloads":
        return[" Data center workloads are diverse. On one hand they are scaling in size and complexity to train advanced AI models. And on the other hand, they need to support numerous concurrent requests each requiring a small amount of acceleration. And these demands can vary throughout the day.",

               "The A100 GPU provides elastic acceleration capability by efficiently scaling up to thousands of GPUs with NVLink technology and NVIDIA Mellanox networking or being partitioned into up to seven isolated GPU instances with MIG to accelerate workloads of all sizes. This enables optimal utilization and adaptability for accelerating all kinds of workloads"]

    elif query == "ask_dgx_a100_v100_speed_ups":
        return ["We are seeing 6X speedup on BERT-Large FP32 training (TF32 Tensor Core is used on A100 GPUs). For popular HPC applications such as LAMMPS, NAMD, and RTM, we see speedups ranging from 1.5X to 2X."]

    elif query == "ask_dgx_a100_mig":
        return ["MIG is a technology that partitions a single A100 GPU into multiple smaller GPU instances. Each instance is like a standalone GPU for the applications. There can be up to seven MIG instances. For example, on an A100 GPU with 40 GB users can create two MIG instances with 20 GB of memory each, three instances with 10 GB or seven with 5 GB. Or create the mix that’s right for target workloads. A full A100 GPU is best for demanding HPC and AI training workloads. MIG instances are good for less demanding workloads as those shown in the table below."]

    elif query == "ask_dgx_a100_mig_workload_instances":
        return ["Yes. Each instance is like a separate GPU and so can run any GPU workload. E.g. one instance can run LAMMPS HPC, some others can run Jupyter notebooks and the remaining TensorFlow training."]

    elif query == "ask_dgx_a100_position":
        return ["The NVIDIA DGX A100 system is the third-generation DGX system and is a universal system for all AI workloads, offering unprecedented compute density, performance, and flexibility in the world’s first 5 petaFLOPS AI system. The world’s first AI system built on the revolutionary NVIDIA A100 Tensor Core GPU, the DGX A100 system unifies data center AI infrastructure, running training, inference, and analytics workloads simultaneously with ease. More than a server, the DGX A100 system is the foundational building block of AI infrastructure and part of the NVIDIA end-to-end data center solution created from over a decade of AI leadership by NVIDIA. The DGX A100 system integrates exclusive access to DGXperts, a global team of AI-fluent practitioners that offer prescriptive planning, deployment, and optimization expertise to help fast-track AI transformation."]

    elif query == "ask_dgx_a100_benefits":
        return ["The DGXA100 systems extend the reach of AI throughout the whole organization, spanning data analysts, data scientists, and IT/DevOps.",
                "-> One system for AI workloads: customers can consolidate individual clusters of training, inference, and data analytics into one cluster of the DGX A100 system",
                "-> Improved system utilization: with Multi-Instance GPU (MIG)",
                "-> Mix and Match workloads: by configuring some GPUs for big training jobs, some GPUs for data analytics jobs and some GPUs in MIG for inference. For example, on DGX A100 with eight GPUs:",
                "• Four GPUs for DL training",
                "• Two GPUs for HPC applications or Data Analytics",
                "• Two GPUs in MIG, creating 14 MIG devices for NVIDIA TensorRT Inference",
                "-> Built-in Security: with new security features in the hardware, firmware, and software"]

    elif query == "ask_dgx_a100_required_cuda":
        return ["DGX A100 systems require CUDA 11. CUDA® 11 was developed for the NVIDIA A100 GPU. CUDA 11 is integrated into DGX software stack to provide all the benefits of the A100 GPU, including MIG, new precisions and performance speedups for different workloads."]

    elif query == "ask_dgx_a100_dgx1_dgx2":
        return ["On all benchmarks, the DGX A100 system is faster than either DGX-1 or DGX-2 systems.", " ",

                "The DGX A100 system is designed for air-cooled, like DGX-2 and DGX-1 systems and can be added into data centers with DGX-1 and DGX-2 systems. The operating temperature range for DGX A100 system is 5 degree Celcius - 30 degree Celcius.", " ",

                "For detailed comparisons, work with your local SAs."]

    elif query == "ask_dgx_a100_price":
        return ["USD$199,000 list price per system and USD$40,000 for three years of system and software support (longer support contracts are available). Installation service is mandatory, pricing available from your chosen NPN. Note that end user pricing is set by our local DGX A100 NPNs. Check with your local DGX specialist.",

                "Pricing for the existing DGX products remain the same. See NVIDIA price list for specific product pricing."]

    elif query == "ask_dgx_a100_dgxperts":
        return ["DGXperts are the collective group of NVIDIA AI-fluent experts across our SA team, engineering, and the wider NVIDIA organization, who use their know-how to help DGX customers get faster answers to questions"]

    elif query == "ask_dgx_a100_access_dgxperts":
        return ["DGXperts are a value-added capability available only to customers who have bought a DGX system (DGX-1, DGX-2, DGX A100, DGX Station).",

                "Customers who need advice on an AI problem/question should consult their SA, who is essentially their lead DGXpert in the relationship. The SA can request/marshal other NVIDIA resources to assist if necessary."]

    elif query == "ask_dgx_a100_fault_tolerance":
        return ["The system has redundant PSUs and mirrored boot drives. Also, memory is ECC protected. The GPUs are connected to all the NVSwitch chips, so if one were to fail the others would keep the communication alive. Network cards can be used in redundant mode and more"]

    elif query == "ask_dgx_a100_vgpu_supported":
        return ["DGX A100 system does not support NVIDIA vGPU."]

    elif query == "ask_dgx_a100_pod":
        return ["The NVIDIA DGX POD™ reference architecture provides a blueprint for large-scale development and deployment of artificial intelligence (AI) software. Although today’s software exceeds the capabilities and accuracy of traditional software, it requires a supercomputer-class system such as the DGX POD. All SAE docs related to the DGX POD (and SuperPOD) can be found on GPU Genius at: https://nvidia.highspot.com/search?q=nvpod.", " ",

                "We continue to leverage NVIDIA DGX POD as a prescriptive infrastructure solution for organizations that want to deploy AI at scale.", " ",

                "Our original DGX POD solutions were targeted at enabling AI training at scale, using a shared, centralized infrastructure approach. Now the value proposition of DGX POD expands to include all AI workloads, inclusive of data analytics as well as inference. For customers, this means that DGX POD provides an end to end infrastructure for AI development to deployment, within the data center."

                ]

    elif query == "ask_dgx_a100_super_pod":
        return ["The NVIDIA DGX SuperPOD reference architecture is based on scalable units of 20 DGX A100 systems, NVIDIA Mellanox networking, DGX POD certified storage, and NVIDIA NGC optimized software.", " ",

                "As part of our DGX SATURNV infrastructure, we’ve deployed the first of our second-generation NVIDIA DGX SuperPOD superclusters, built on DGX A100 systems. This expansion within SATURNV adds over 140 DGX A100 systems, capable of 700 PFLOPS of AI performance. Over time additional DGX SuperPOD configurations with DGX A100 systems will be added", " ",

                "All SAE docs related to the DGX SuperPOD) can be found on GPU Genius at: ", " ",
                "https://nvidia.highspot.com/search?q=NVPOD-Super"]

    elif query == "ask_dgx_a100_software_program":
        return ["The NVIDIA DGX-Ready™ Software program is a new program for DGX customers that delivers NVIDIA- certified third-party platforms on top of a cluster of DGX systems. The first batch of these programs focuses on AI workflow solutions which improve data science team productivity, accelerate AI pipelines, and increase utilization of compute resources."]

    elif query == "ask_dgx_a100_buy_support_services":
        return ["DGX A100 Support Services are mandatory for each product purchase on the order. The purchase quantity of required services must equal the product quantity. (Each system must be accompanied by a service contract). You can choose either of DGX A100 Support services (3- or 5-year SKU) when purchasing the product",
                " ",
                "List Price (US$)",
                "-> DGX A100 System 8X 40GB GPUs Support, 3 Years $40,000",
                "-> DGX A100 System 8X 40GB GPUs Support, 5 Years $63,333",

                "A DGX A100 system order must also include one of the following installation SKUs. Note, installation by NPN partner is the mandatory SKU for all standard sales."]

    elif query == "ask_dgx_a100_argonne":
        return ["Argonne National Laboratory is the world's first DGX A100 Supercomputer fighting COVID-19. It has 24-node Cluster of DGX A100 Systems, 192 A100 GPUs, Mellanox High-Speed Low-Latency Network Fabric, and 120 PetaFLOPSof AI Computing Power for Scientific Research"]

    elif query == "ask_dgx_a100_selene":
        return [
            "AI and HPC continue to expand the frontiers of exploration, but today’s most challenging opportunities require a new architecture that can deliver unprecedented levels of computing scale to drive faster insights from massive volumes of data. Where traditional high-performance compute clusters take months or years to deploy, NVIDIA’s Selene supercomputer, built on the NVIDIA DGX SuperPOD™ reference architecture, offers a faster path to massive scale, in a Top10-class supercomputer that was deployed in under a month. Join us for this special insider’s look at how Selene and the DGX SuperPOD are redefining AI infrastructure. We’ll explore what fueled Selene’s design, how it can be deployed as a commercially available turnkey solution, how we rapidly deployed Selene using it’s modular design and ability to incrementally scale, and the tools we use to run mission-critical mixed workloads.",
            " ",
            "4480 A100 GPUs, 560 DGX A100 Systems",
            "850 Mellanox 200G HDR switches",
            "14 PB of high-performance storage",
            "2.8 EFLOPS of AI peak performance",
            "63 PFLOPS HPL @ 24GF/W"
        ]

    elif query == "ask_dgx_a100_tpm":
        return [
            "The NVIDIA DGX A100 system supports self-encrypted drives and Trusted Platform Module(TPM) technology for added security.",
            " ",
            "The NVIDIA DGX A100 system includes a secure cryptoprocessor which conforms to the Trusted Platform Module(TPM 2.0)2 industry standard. The cryptoprocessor is the foundation of the security subsystem in the DGX A100, securing hardware via cryptographic operations.When enabled, The TPM ensures the integrity of the boot process until the DGX OS has fully booted and applications are running. The TPM is also used with the self-encrypting drives and the drive encryption tools for secure storage of the vault and SED authentication keys.",
            " ",
            "See the Trusted Platform Module white paper from the Trusted Computing group https://trust-edcomputinggroup.org/resource/trusted-platform-module-tpm-summary /"
        ]

    elif query == "ask_dgx_seds":
        return [
            "The NVIDIA DGX A100 system supports self-encrypted drives and Trusted Platform Module(TPM) technology for added security.",
            " ",
            "The NVIDIA DGX™ OS software supports managing self-encrypting drives(SEDs). SEDs encrypt data on the drives automatically without user intervention. For additional security, DGX allows configuration of an Authentication Key so that drives lock on shut down, requiring the key to be entered at power on to unlock the drives for use."
        ]

    elif query == "ask_dgx_tensor_cores":
        return [
            "The NVIDIA A100 GPU includes new third-generation Tensor Cores. Tensor Cores are specialized high-performance compute cores that perform mixed-precision matrix multiply and accumulate calculations in a single operation, providing accelerated performance for AI workloads and HPC applications.",

            " ",

            "The first-generation Tensor Cores used in the NVIDIA DGX-1 with NVIDIA V100 provided accelerated performance with mixed-precision matrix multiply in FP16 and FP32. This latest generation in the DGX A100 uses larger matrix sizes, improving efficiency and providing twice the performance of the NVIDIA V100 Tensor Cores along with improved performance for INT4 and binary data types. The A100 Tensor Core GPU also adds the following new data types:",

            " ",

            "1. TensorFloat-32 (TF32)",
            "2. IEEE Complaint FP64",
            "Bfloat16(BF16)"
        ]

    elif query == "ask_dgx_a100_sparsity":
        return [
            "The NVIDIA A100 GPU supports fine-grained structured sparsity to accelerate simplified neural networks without harming accuracy. Sparsity often comes from pruning - the technique of removing weights that contribute little to the accuracy of the network. Typically, this involves 'zeroing out' and removing weights that have zero or near-zero values. In this way, pruning can convert a dense network into a sparse network that delivers the same level of accuracy with reduced compute, memory, and energy requirements. Until now, though, this type of fine-grained sparsity did not deliver on its promises of reduced model size and faster performance.",

            " ",

            "With fine-grained structured sparsity and the 2:4 pattern supported by A100(Figure 6), each node in a sparse network performs the same amount of memory accesses and computations, which results in a balanced workload distribution and even utilization of compute nodes. Additionally, structured sparse matrices can be efficiently compressed, and their structure leads to doubled throughput of matrix multiply-accumulate operations with hardware support in the form of Sparse Tensor Cores.",

            " ",

            "The result is accelerated Tensor Core computation across a variety of AI networks and increased inference performance. With fine-grained structured sparsity, INT8 Tensor Core operations on A100 offer 20X more performance than on V100, and FP16 Tensor Core operations are 5X faster than on V100"
        ]

    elif query == "ask_dgx_a100_network_throughput":
        return [
            "Multi-system scaling of AI deep learning and HPC computational workloads requires strong communications between GPUs in multiple systems to match the significant GPU performance of each system. In addition to NVLink for high-speed communication internally between GPUs, the DGX A100 is purpose-built for multi-system AI scaling with eight single-port Mellanox ConnectX-6 200Gb/s HDR InfiniBand ports(also configurable as 200Gb/s Ethernet ports) providing 3.2 Tb/s of peak bandwidth from a single system that can be used to immediately build a high-speed cluster of DGX A100 systems such as NVIDIA DGX SuperPOD.",
            " ",
            "The most common methods of moving data to and from the GPU involve leveraging the on-board storage and using the Mellanox ConnectX-6 network adapters through Remote Direct Memory Access(RDMA). The DGX A100 incorporates a one-to-one relationship between the IO cards and the GPUs, which means each GPU can communicate directly with external sources without blocking other GPUs' access to the network",

            " ",

            "The Mellanox ConnectX-6 I/O cards offer flexible connectivity as they can be configured as HDR InfiniBand or 200Gb/s Ethernet. This allows the NVIDIA DGX A100 to be clustered with other nodes to run HPC and AI workloads using low latency, high bandwidth InfiniBand, or RDMA over Converged Ethernet(RoCE)"
        ]

    elif query == "ask_dgx_a100_pcie_gen4":
        return [
            "The NVIDIA A100 GPUs are connected to the PCI switch infrastructure over x16 PCI Express Gen 4 (PCIe Gen4) buses that provide 31.5 Gb/s each for a total of 252 Gb/s, doubling the bandwidth of PCIe 3.0/3.1. These are the links that provide access to the Mellanox ConnectX-6, the NVMe storage, and the CPU"
        ]

    elif query == "ask_dgx_a100_nvme":
        return [
            "Training workloads commonly involve reading the same datasets many times to improve accuracy. Rather than use up all the network bandwidth to transfer this data over and over, high performance local storage is implemented with NVMe drives to cache this data. This increases the speed at which the data is read into memory, and it also reduces network and storage system congestion.",

            " ",

            "Each DGX A100 system comes with dual 1.92 TB NVMe M.2 boot OS SSDs configured in a RAID 1 volume, and four 3.84 TB PCIe gen4 NVMe U.2 cache SSDs configured in a RAID 0 volume. The base RAID 0 volume has a total capacity of 15 TB, but an additional 4 SSDs can be added to the system for a total capacity of 30 TB. These drives use CacheFS to increase the speed at which workloads access data and to reduce network data transfers."
        ]

    elif query == "ask_dgx_a100_software_stack":
        return [
            "The DGX A100 software has been built to run AI workloads at scale. A key goal is to enable practitioners to deploy deep learning frameworks, data analytics and HPC applications on the DGX A100 with minimal setup effort. The design of the platform software is centered around a minimal OS and driver install on the server, and provisioning of all application and SDK software available through the NGC Private Registry.",
            " ",
            "The NGC Private Registry provides GPU-optimized containers for deep learning(DL), machine learning(ML), and high performance computing(HPC) applications, along with pretrained models, model scripts, Helm charts, and software development kits(SDKs). This software has been developed, tested, and tuned on DGX systems, and is compatible with all DGX products: DGX-1, DGX-2, DGX Station, and DGX A100.  The NGC Private Registry also provides a secure space for storing custom containers, models, model scripts, and Helm charts that can be shared with others within the enterprise. Learn more about the NGC Private Registry in this blog post"
        ]

    elif query == "ask_nvidia_container_toolkit":
        return [
            "The NVIDIA Container Toolkit allows users to build and run GPU accelerated Docker containers. The toolkit includes a container runtime library and utilities to automatically configure containers to leverage NVIDIA GPUs.",
            " ",
            "GPU-accelerated containers feature software to support > Deep learning frameworks for training, such as PyTorch, MXNet, and TensorFlow > Inference platforms, such as TensorRT > Data analytics, such as RAPIDS, the suite of software libraries for executing end-to-end data science and analytics pipelines entirely on GPUs. > High-Performance Computing(HPC), such as CUDA-X HPC, OpenACC, and CUDA®."
        ]

    elif query == "ask_nvidia_cuda_toolkit":
        return [
            "CUDA is a parallel computing platform and programming model created by NVIDIA. With more than 20 million downloads to date, CUDA helps developers speed up their applications by harnessing the power of GPU accelerators.",
            " ",

            "The NVIDIA CUDA Toolkit, incorporated within each GPU-accelerated container, is the development environment for creating high performance GPU-accelerated applications.CUDA 11 enables software developers and DevOps engineers to reap the benefits of the major innovations in the new NVIDIA A100 GPU, including the following",

            "Support for new input data type formats, Tensor Cores and performance optimizations in CUDA libraries for linear algebra, FFTs, and matrix multiplication > Configuration and management of MIG instances on Linux operating systems, part of the DGX software stack > Programming and APIs for task graphs, asynchronous data movement, fine-grained synchronization, and L2 cache residency control"
        ]

    elif query == "ask_dgx_a100_mlperf":
        return [
            "In MLPerf, the industry-standard benchmark for machine learning, NVIDIA DGX A100 as a single node and DGX SuperPOD, cluster of DGX A100 systems, demonstrated world-class performance and versatility. NVIDIA DGX SuperPOD, combining multiple NVIDIA DGX A100 systems with NVIDIA Mellanox network fabric, gives businesses a proven formula to shorten their design and deployment cycles.",
            " ",
            "NVIDIA DGX SuperPOD with DGX A100 systems set world records for fastest time to solution in all 8 of the at scale benchmarks in MLPerf v0.7 Training and the NVIDIA A100 GPU also demonstrated fastest per accelerator performance overall in the commercially available systems category. The commercially available systems category submissions represent the state of the art of hardware and software that is available for the industry to benefit from today.",
            " ",
            "The MLPerf v0.7 training benchmark suite includes vision, language, recommenders, and reinforcement learning workloads."
        ]

    elif query == "ask_dgx_front_fan_replace":
        return [
            "1. Identify the failed front fan module through the BMC or the fan module LED and submit a service ticket to NVIDIA Enterprise Support.",

            "Type: sudo nvsm show fans. In the output, look for the 'unhealthy' status for the same fan.",

            "2. Get a replacement from NVIDIA Enterprise Support.",

            "3. Remove the failed fan module using the fan numbering diagram as a reference.",

            "4. Insert the new fan module.",

            "5. Confirm the new fan module is working correctly through the BMC or NVSM. Type: sudo nvsm show health",

            "6. Return the bad fan module using the packaging from the new fan module.",

            " ",

            "See details: https://docs.nvidia.com/dgx/dgxa100-service-manual/front-fan-replacement.html"
        ]

    # typo spotted
    elif query == "ask_dgx_pwoer_supply":
        return [
            "1. Identify failed power supply through the BMC and submit a service ticket.",

            "2. Type: sudo nvsm show psus. The output shows information for each PSU. Look for any that do not report Status_Health = OK.",

            "3. Type: sudo ipmitool sdr | grep - i psu. Look for power supplies with no temperature reading or an output reading close to or equal to zero.",

            "4. Get replacement power supply from NVIDIA Enterprise Support.",

            "5. Identify the power supply using the diagram as a reference and the indicator LEDs.",

            "6. Remove the power cord from the power supply that will be replaced.",

            "7. Replace the failed power supply with the new power supply.",

            "8. Insert the power cord and make sure both LEDs light up green(IN/OUT).",

            "9. Use the BMC to confirm that the power supply is working correctly.",

            "10. Ship back the failed unit to NVIDIA Enterprise Support using the packaging provided.",

            " ",

            "See details: https://docs.nvidia.com/dgx/dgxa100-service-manual/psu-replacement.html",

        ]

    elif query == "ask_dgx_access_motherboard":
        return [
            "You will need to access the motherboard tray in order to service the following components. This process provides access to the motherboard components while the motherboard remains attached to the server.",

            "1. Loosen the two motherboard thumbscrews and then pull the handles out to eject the motherboard tray",

            "2. Pull the motherboard tray out of the system until it locks, then loosen the two thumbscrews holding the lid in place.",

            "3. Lift the rear section of the motherboard lid.",

            "To replace the motherboard try:",

            "1. Close the lid to the motherboard tray.",

            "2. Tighten the two thumbscrews and then push the motherboard tray into the system",

            "3. Close the handles to secure the motherboard tray in place.",

            "4. Tighten the motherboard tray thumbscrews to complete the motherboard insertion."
        ]

    elif query == "ask_dgx_remove_install_motherboard":
        return [
            "You will need to completely remove the motherboard tray from the server in order to service DIMMs(either adding or replacing)",

            "To remove the motherboard try",

            "1. Loosen the two motherboard thumbscrews and then pull the handles out to eject the motherboard tray.",

            "2. Pull the motherboard tray out of the system until it locks, then press the two buttons on the top of the lid to release the tray and finish pulling the tray out of the system.",

            "3. Loosen two rear thumbscrews on the motherboard lid.",

            "4. Loosen the two front thumbscrews on the motherboard tray lid.",

            "5. Lift the lid off of the tray and set aside.",

            "6. Remove all three air baffles to allow access to the DIMMs.",

            " ",

            "To reinstall the motherboard tray",

            "1. Reinstall the three air baffles.",

            "2. Replace and secure the lid.",

            "3. Slide the motherboard tray into the slot, open the tray handles, and then continue pushing the motherboard tray in .",

            "4. Close the handles to secure the motherboard tray in place.",

            "5. Tighten the motherboard tray thumbscrews to complete the motherboard insertion."
        ]

    elif query == "ask_dgx_a100_u2_determine_drive":
        return [
            "1. Identify the drives in the RAID volume by issuing the following",

            "sudo nvme list",

            "2. Determine the drive size (3.84 TB or 7.68 TB) of the currently installed drives, and order drives of same density (capacity) from the NVIDIA Sales team.",

            " ",

            "Note: If 3.84 TB drives are installed but you want to use or add 7.68 TB drives, refer to https://docs.nvidia.com/dgx/dgxa100-service-manual/u2-nvme-upgrade-to-8tb.html#u2-nvme-upgrade-to-8tb for instructions."

        ]

    elif query == "ask_dgx_a100_u2_upgrade_nvme_cache":
        return [
            "This is a high-level overview of the steps needed to upgrade the DGX A100 system's cache size.",

            "1. Identify the density(capacity) of the currently installed NVMe drives.",

            "2. Place an order for additional four NVME drives from NVIDIA Sales.",

            "3. Power off the system.",

            "4. Remove the air baffles in the blank drive slots.",

            "5. Install the NVMe drives in the DGX A100 system.",

            "6. Power on the system.",

            "7. Re-initialize the / raid filesystem to recognize all eight drives.",

            "8. Confirm the system is healthy by running nvsm show health."

        ]

    elif query == "ask_dgx_a100_u2_nvme_add_drives":
        return [
            "To install the optional nvme drives, please check https://docs.nvidia.com/dgx/dgxa100-service-manual/u2-nvme-upgrade-4-to-8.html#u2-nvme-adding-drives"
        ]

    elif query == "ask_dgx_a100_u2_identify_failed_dirve":
        return [
            "If physical access to the system is available, you can identify a failed drive by the illuminated amber LED.",

            "To identify the failed NVMe drive from the DGX A100 console, enter the following and then look for drive alerts in the output to identify the failed drive.",

            "sudo nvsm show health",

            " ",

            "For more details, please check https://docs.nvidia.com/dgx/dgxa100-service-manual/u2-nvme-replacement.html#identifying-failed-u2-nvme."

        ]

    elif query == "ask_dgx_a100_u2_replace_nvme":
        return [
            "To replace the U.2 NVME Drive, check https://docs.nvidia.com/dgx/dgxa100-service-manual/u2-nvme-replacement.html#identifying-failed-u2-nvme."
        ]

    elif query == "ask_dgx_a100_u2_upgrade_nvme768":
        return [
            "This is a high-level overview of the steps needed to upgrade the DGX A100 system's cache size.",

            "1. Place an order for the 7.68 TB U.2 NVMe drives from NVIDIA Sales.",

            "2. Power off the system.",

            "3. Remove the existing components. Remove all 3.84 TB cache drives. If you are also upgrading from four to eight cache drives, then remove the air baffles in the blank drive slots.",

            "4. Install the 7.68 TB NVMe drives in the DGX A100 system.",

            "5. Power on the system.",

            "6. Re-initialize the / raid filesystem to recognize all eight drives.",

            "7. Confirm the system is healthy by running nvsm show health."
        ]

    elif query == "ask_dgx_a100_u2_nvme_postinstall":
        return [
            "2 tasks that are typically needed after replacing a U.2 NVME drive or upgrading from 4 to 8 drives,",

            "1. Recreate the Cache RAID 0 Volume",

            "2. Return the NVME Drive",

            " ",

            "For more details, check https://docs.nvidia.com/dgx/dgxa100-service-manual/u2-nvme-post-installation.html#u2-nvme-post-installation"
        ]

    elif query == "ask_dgx_operation_prepare":
        return [
            "DGX OS 5 is preinstalled on new DGX systems. A setup wizard in the First Boot procedure requires you to create a user, set locales and keyboard layout, set passwords, and perform basic network configuration.",

            "For systems that are running DGX OS version 4, you can upgrade the system to DGX OS 5 from network repositories (distribution upgrade) or reimage the system from the DGX OS 5 ISO image. The reimaging process installs the OS but defers the initial setup to the First Boot Process for DGX Servers or First Boot Process for DGX Station.",

            "During the initial installation and configuration steps, you need to connect to the console of the DGX system.",

            "There are several ways to connect to the DGX system, including the following",

            " ",

            "1. Through a virtual keyboard, video, and mouse (KVM) in the BMC.",

            "2. A direct connection with a local monitor and keyboard.",

            " ",

            " Also, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#dgx-set-up for set up instructions.",

            " for details, please see https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#preparing",

        ]

    elif query == "ask_dgx_install_os":
        return [
            "Installing DGX OS erases all data stored on the OS drives. This includes the / home partition, where all users' documents, software settings, and other personal files are stored. If you need to preserve data through the reimaging, you can move the files and documents to the / raid directory and install the DGX OS software with the option to preserve the RAID array content. The reimage process does not change persistent hardware configurations such as MIG settings or data drive encryption.",

            "First, you have to Obtain the latest DGX OS ISO image from NVIDIA Enterprise Support(ensure that you have an NVIDIA Enterprise Support account)",

            "Then, Install the DGX OS ISO image in one of the following ways:",

            "1. Remotely through the BMC for systems that provide a BMC. Refer to Reimaging the System Remotely for instructions. This method is not available for DGX Station.",

            "2. Locally from a UEFI-bootable USB flash drive or DVD-ROM. Refer to Installing the DGX OS Image from a USB Flash Drive or DVD-ROM for instruction.",

            " ",

            "For details, please see https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#install-dgx-os"
        ]

    elif query == "ask_dgx_post_installation":
        return [
            "You can complete the following tasks after you install your DGX sytem.",

            " ",

            "Adding Support for Additional Languages to the DGX Station",

            "Configuring your DGX Station To Use Multiple Displays",

            "Enabling Multiple Users to Remotely Access the DGX System",

            " ",

            "For details, please see https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html"
        ]

    elif query == "ask_dgx_upgrade_os":
        return [
            "The upgrade procedures consist of 5 steps:",

            "1. Get Release Information for DGX Systems. To get release information for the DGX system, view the content of the /etc/dgx-release file.",

            "2. Connect to the console of the DGX system using a direct connection or a remote connection through the BMC.",

            "3. Before you attempt to complete the update, verify that the network connection for your DGX system can access the public repositories and that the connection is not blocked by a firewall or proxy.",

            "4. Upgrade your DGX OS and verify the updates",

            "5. Manage Software Upgrades on the Desktop and check for Updates to DGX Station Software",

            " ",

            "For details, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#upgrading-os-5"
        ]

    elif query == "ask_dgx_additional_software":
        return [
            "DGX OS 5 is an optimized version of the Ubuntu 20.04 Linux distribution with access to a large collection of additional software that is available from the Ubuntu repositories. You can install the additional software using the apt command or through a graphical tool.",

            "1. Identify and change your GPU branch: On your DGX system, you should only install the packages that include the NVIDIA Data Center GPU drivers. The metapackages for the NVIDIA Data Center GPU driver have the -server suffix .",

            "2. Install or Upgrade CUDA Toolkit: Only DGX Station and DGX Station A100 have a CUDA Toolkit release installed by default. DGX servers are intended to be shared resources that use containers and do not have CUDA Toolkit installed by default. However, you have the option to install a qualified CUDA Toolkit release. Although the DGX OS supports all CUDA Toolkit releases that interoperate with the installed driver, DGX OS releases might include a default CUDA Toolkit release that might not be the most recently released version. Unless you must use a new CUDA Toolkit version that contains the new features, we recommend that you remain on the default version that is included in the DGX OS release. Refer to the DGX OS Software Release Notes for the default CUDA Toolkit release.",

            "3. Install GPUDirect Storage Support: NVIDIA® Magnum IO GPUDirect® Storage (GDS) enables a direct data path for direct memory access (DMA) transfers between GPU memory and storage, which avoids a bounce buffer through the CPU.",

            " ",

            "For details, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#install-addl-sw"

        ]

    elif query == "ask_dgx_network_config":
        return [
            "The components of network configurations for DGX sustem include:",

            "1. Configuration of Network Proxies: If your network needs to use a proxy server, you need to set up configuration files to ensure the DGX system communicates through the proxy.",

            "2. Preparing the DGX System to be Used With Docker: Some initial setup of the DGX system is required to ensure that users have the required privileges to run Docker containers and to prevent IP address conflicts between Docker and the DGX system. Some initial setup of the DGX system is required to ensure that users have the required privileges to run Docker containers and to prevent IP address conflicts between Docker and the DGX system.",

            "3. DGX OS Connectivity Requirements: In a typical operation, DGX OS runs services to support typical usage of the DGX system. Some of these services require network communication. The table below describes the port, protocol, direction, and communication purpose for the services. DGX administrators should consider their site-specific access needs and allow or disallow communication with the services as necessary.",

            "4. Connectivity Requirements for NGC Containers: To run NVIDIA NGC containers from the NGC container registry, your network must be able to access nvcr.io and some other URLs like https://apt.dockerproject.org/repo/",

            "5. Configuring Static IP Addresses for the Network Ports",

            " ",

            "For details, please check: https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#network-config",

        ]

    elif query == "ask_dgx_manage_cpu_mitigation":
        return [
            "DGX OS software includes security updates to mitigate CPU speculative side-channel vulnerabilities. These mitigations can decrease the performance of deep learning and machine learning workloads.",

            "If your DGX system installation incorporates other measures to mitigate these vulnerabilities, such as measures at the cluster level, you can disable the CPU mitigations for individual DGX nodes and increase performance.",

            "To determine the CPU Mitigation State of the DGX System, check the following",

            "cat /sys/devices/system/cpu/vulnerabilities/* ",

            "CPU mitigations are enabled when the output consists of multiple lines prefixed with Mitigation:. CPU mitigations are disabled if the output consists of multiple lines prefixed with Vulnerable.",

            "To disable CPU mitigations, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#disable-cpu-mitigations",

            " ",

            "To re-enable CPU mitigations, please check  https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#reenable-cpu-mitigations"
        ]

    elif query == "ask_dgx_crash_dump":
        return [
            "You can use the script that is included in the DGX OS to manage DGX Crash Dump Feature.",

            "to enable only dmesg crash dumps, run / usr/sbin/nvidia-kdump-config enable-dmesg-dump",

            "to enable both dmesg and vmcore crash dumps, run / usr/sbin/nvidia-kdump-config enable-vmcore-dump",

            "to disable crash dumps, run / usr/sbin/nvidia-kdump-config disable",

            " ",

            "to connect to serial over LAN, run: ipmitool - I lanplus - H - U - P sol activate"
        ]

    elif query == "ask_dgx_a100_update_containerd":
        return [
            "When you add MIG instances, the containerd overrride file does not automatically get updated, and the new MIG instances that you add will not be added to the allow file.",

            "When DGX Station A100 starts, after the nv-docker-gpus service runs, a containerd override file is created in the /etc/systemd/system/containerd.service.d/ directory.",

            "Note: This file blocks Docker from using the display GPU.",

            " ",

            "Here is an example of an override file:",

            "[Service]",

            "DeviceAllow=/dev/nvidia1",

            "DeviceAllow=/dev/nvidia2",

            "DeviceAllow=/dev/nvidia3",

            "DeviceAllow=/dev/nvidia4",

            "DeviceAllow=/dev/nvidia-caps/nvidia-cap1",

            "DeviceAllow=/dev/nvidia-caps/nvidia-cap2",

            "DeviceAllow=/dev/nvidiactl",

            "DeviceAllow=/dev/nvidia-modeset",

            "DeviceAllow=/dev/nvidia-uvm",

            "DeviceAllow=/dev/nvidia-uvm-tools",

            " ",

            "For details, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#update-containerd-override-file",

        ]

    elif query == "ask_dgx_config_storage":
        return [
            "By default, the DGX system includes several drives in a RAID 0 configuration. These drives are intended for application caching, so you must set up your own NFS storage for long-term data storage.",

            "From the factory, the RAID level of the DGX RAID array is RAID 0. This level provides the maximum storage capacity, but it does not provide redundancy. If one SSD in the array fails, the data that is stored on the array is lost. If you are willing to accept reduced capacity in return for a level of protection against drive failure, you can change the level of the RAID array to RAID 5.",

            "To change the RAID level to RAID 5, run sudo configure_raid_array.py - m raid5",

            "To change the RAID level to RAID 0, sudo configure_raid_array.py - m raid0",

            " ",

            "To see more details about how NFS is managed in DGX system, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#data-storage-config"

        ]

    elif query == "ask_dgx_run_ngc":
        return [
            "NVIDIA NGC provides simple access to GPU-optimized software for deep learning, machine learning , and high-performance computing (HPC). An NGC account grants you access to these tools and gives you the ability to set up a private registry to manage your customized software.",

            "If you are the organization administrator for your DGX system purchase, work with NVIDIA Enterprise Support to set up an NGC enterprise account. Refer to the NGC Private Registry User Guide for more information about getting an NGC enterprise account.",

            "To obtain the best performance when running NGC containers on DGX systems, you may use either Native GPU support or NVIDIA Container Runtime for Docker",

            " ",

            "For more details, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#run-ngc-cont-gpu-supp"

        ]

    elif query == "ask_dgx_air_gapped":
        return [
            "For security purposes, some installations require that systems be isolated from the internet or outside networks.",

            "An air-gapped system is not connected to an unsecured network, such as the public Internet, to an unsecured LAN, or to other computers that are connected to an unsecured network. The default mechanisms to update software on DGX systems and loading container images from the NGC Container Registry require an Internet connection. On an air-gapped system, which is isolated from the Internet, you must provide alternative mechanisms to update software and load container images.",

            "Since most DGX software updates are completed through an over-the-network process with NVIDIA servers, this section explains how updates can be made when using an over-the-network method is not an option. It also includes a process to install Docker containers.",

            " ",

            "For more details, please check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#install-softw-ag-dgx-systems"
        ]

    elif query == "ask_dgx_pxe_boot":
        return [
            "To set up network and the DGX server so that the server boots from it using the preboot execution environment (PXE), plaese check https://docs.nvidia.com/dgx/dgx-os-5-user-guide/index.html#set-up-pxe-boot"
        ]

    elif query == "ask_dgx_authenticating_user":
        return [
            "To make the DGX useful, users need to be added to the system in some fashion so they can be authenticated to use the system. Generally, this is referred to as user authentication. There are several different ways this can be accomplished, however, each method has its own pros and cons.",

            "Example of adding users using useradd command:",

            "To add a user 'dgxuser1', run useradd -m -s /bin/bash dgxuser",

            "Then, you may add that user to docker group by running sudo usermod -aG docker dgxuser",

            " ",

            "For other options to add users, such as NIS, NIS+, LDAP, Active Directory, please check https://docs.nvidia.com/dgx/bp-dgx/users.html#users",

        ]

    elif query == "ask_dgx_time_sync":
        return [
            "Time synchronization is very important for clusters of systems including storage. It is especially true for MPI (Message Passing Interface) applications such as those in the HPC world. Without time synchronization, you can get wrong answers or your application can fail. Therefore, it is a good idea to sync the DGX-2, DGX-1, or DGX Station time.",

            "for more information and instructions, you can run",

            "man timedatectl command",

            "man systemd-timesyncd.service",

            " ",

            "For more details. run https://docs.nvidia.com/dgx/bp-dgx/time.html#time"

        ]

    elif query == "ask_dgx_manage_resources":
        return [
            "Everything on the DGX system can be viewed as a resource. This includes memory, CPUs, GPUs, and even storage. Users submit a request to the resource manager with their requirements and the resource manager assigns the resources to the user if they are available and not being used. Otherwise, the resource manager puts the request in a queue to wait for the resources to become available. When the resources are available, the resource manager assigns the resources to the user request. This request is known as a 'job''.",

            "A resource manager provides functionality to act on jobs such as starting, canceling, or monitoring them . It manages a queue of jobs for a single cluster of resources, each job using a subset of computing resources. It also monitors resource configuration and health, launching jobs to a single FIFO queue.",

            "A job scheduler ties together multiple resource managers into one integrated domain, managing jobs across all machines in the domain. It implements policy mechanisms to achieve efficient utilization of resources,manages software licenses, and collects and reports resource usage statistics",

            "Resource managers and job schedulers have been around for a long time and are extensively used in the HPC world.You may run solutions in DGX system such as SLURM, Univa Grid Engine, IBM Spectrum LSF, and Altair PBS Pro. If you haven't used these tools before, you should perform some simple experiments first to understand how they work. For example, take a single server and install the software, then try running some simple jobs using the cores on the server. Expand as desired and add more nodes to the cluster.",

            " ",

            "For more instructions, plase check https://docs.nvidia.com/dgx/bp-dgx/resources.html#resources."
        ]

    elif query == "ask_dgx_cluster_manage":
        return [
            "Cluster management tools go beyond resource managers and job schedulers, managing the state of each node in an entire cluster. They typically include mechanisms to provision the nodes in the cluster(install the operating system image, firmware, and drivers), deploy a job scheduler, monitor and manage hardware, configure user access, and make modifications to the software stack.",

            "Provisioning and cluster management of DGX Systems may be bootstrapped with DeepOps. DeepOps is open source and highly modular. It has defaults which can be configured to meet organizational needs and incorporates best practices for deploying GPU-accelerated Kubernetes and Slurm.",

            " ",

            "For details of DeepOps, see https://github.com/NVIDIA/deepops"
        ]

    else:
        return ["I'm sorry, I didn't quite understand that. Could you rephrase?"]


if __name__ == "__main__":
    dgx_resp()
