# NI DOCUMENT BUNDLE: labview-gpu-analysis-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-gpu-analysis-toolkit-api-ref start=1 end=72 -->
<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpu/computing_operations_on_gpu.html language=enus -->
## TOPIC 00001: Performing FFT or BLAS Operations on a GPU Device (GPU Analysis Toolkit)

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpu/computing_operations_on_gpu.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpu/computing_operations_on_gpu.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Performing FFT or BLAS Operations on a GPU Device (GPU Analysis Toolkit)

The GPU Analysis Toolkit allows you to communicate with a graphics processing unit (GPU) from LabVIEW. A GPU can compute large, computationally challenging problems while the CPU works as the primary processor. This functionality results in co-processing for faster performance than if the application uses only the CPU. Large problem sizes and parallel computations can decrease performance because of CPU limitations in both the number of cores and the amount of cache per core; however, GPUs do not have these same limitations. Use the GPU Analysis Toolkit for [designing the block diagram](../lvgpu/designing_bd_for_gpu.html) to offload large FFT or BLAS operations to a GPU device and to upload the results back to the CPU.

|  | Note To use the GPU Analysis Toolkit, you must have the NVIDIA CUDA Toolkit and an NVIDIA display driver. Refer to the readme_GPUAnalysis.html file, located in the labview\\readme directory, for more information about these requirements. |
| --- | --- |

The following figure shows the algorithm flow when offloading FFT operations in a multichannel FFT application. In this figure, blue signifies a process on the CPU and green signifies a process on the GPU.

[IMAGE alt='image' src='gpu-analysi_algorithm_flow.gif']

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpu/designing_bd_for_gpu.html language=enus -->
## TOPIC 00002: Designing the Block Diagram to Compute on a GPU Device (GPU Analysis Toolkit)

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpu/designing_bd_for_gpu.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpu/designing_bd_for_gpu.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing the Block Diagram to Compute on a GPU Device (GPU Analysis Toolkit)

The following illustrations show the common steps for communicating with a GPU device from the block diagram. This workflow applies to offloading either FFT or BLAS operations in a LabVIEW application. To create an application that integrates a GPU, use the [GPU Analysis](../lvgpuvi/lvgpuvi.html) VIs.

The GPU Analysis Toolkit provides an example of an application that offloads FFT operations with both a large data set and a large number of parallel tasks. The following illustrations are taken from the block diagram of the Multi-channel FFT VI in the Multi-channel FFT LabVIEW project, and you can refer to this example in the labview\examples\lvgpu directory to see where these illustrations fit into the entire application design.

|  | Note This example computes the FFTs of simulated signals from multiple simulated channels. In a real application, you might acquire the signal or spectrum input data from a DAQ device or read it from a log file. |
| --- | --- |

#### I. Initializing GPU Resources

[IMAGE alt='image' src='noloc_bd_set_and_allocate.gif']

|  | The Initialize Device VI creates the special execution environment, or context, necessary for LabVIEW to communicate with the GPU. |
| --- | --- |
|  | The Initialize Library VI prepares the GPU for FFT operations by selecting the FFT to compute. The initialization process reserves resources on the GPU device to improve performance. The FFT type includes information on the FFT size, the number of FFTs to perform in parallel on the GPU, and the data type of the input signals or spectrums. You can select from the following types: CUFFT_C2C: (Inverse) Complex FFT – CSG CUFFT_R2C: Real FFT – SGL CUFFT_C2R: Inverse Real FFT – SGL CUFFT_Z2Z: (Inverse) Complex FFT – CDB CUFFT_D2Z: Real FFT – DBL CUFFT_Z2D: Inverse Real FFT – DBL |
|  | The Allocate Memory VI acquires memory in the form of a buffer from the GPU device. The buffer stores both the channel data for downloading onto the GPU (step 4) and the results of the computations performed on the GPU for uploading to the CPU (step 6). |

#### II. Performing FFT Computations on the GPU

[IMAGE alt='image' src='noloc_bd_loop.gif']

|  | Note If you perform the following three steps in a loop, then the application needs only to initialize and release resources once. |
| --- | --- |

|  | The Download Data VI transfers the channels of data—stored in a LabVIEW array—to the buffer on the GPU device allocated in step 3. This example shows the individual channels stored in the rows of a 2D array. You also can download multiple channels stored sequentially in a 1D array. |
| --- | --- |
|  | The FFT VI computes the spectrum simultaneously for each channel downloaded. |
|  | The Upload Data VI transfers the spectral data—stored in a buffer on the GPU device—to a LabVIEW array for use elsewhere on the block diagram. |

#### III. Releasing GPU Resources

[IMAGE alt='image' src='noloc_bd_destroy.gif']

|  | Note Perform the following three steps in the order described. |
| --- | --- |

|  | The Free Memory VI releases the buffer on the GPU that stores the FFT data. |
| --- | --- |
|  | The Release Library VI frees any resources on the GPU reserved since initialization for FFT computations. |
|  | The Release Device VI frees any resources on the GPU device reserved since initialization, including resources for communication with the GPU and any active processes on the GPU that began after initialization. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpu/gpu_error_codes.html language=enus -->
## TOPIC 00003: Error Codes (GPU Analysis Toolkit)

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpu/gpu_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpu/gpu_error_codes.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (GPU Analysis Toolkit)

The [GPU Analysis](../lvgpuvi/lvgpuvi.html) VIs can return the following error codes. For more detailed information about many GPU Analysis errors, see the source string of the error cluster containing the error code in the software. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −359633 | A call to a function in the NVIDIA CUDA driver resulted in an error condition. For more detailed information, see the source string of the error cluster containing the error code. |
| −359632 | A call to a function in the NVIDIA CUFFT library resulted in an error condition. For more detailed information, see the source string of the error cluster containing the error code. |
| −359631 | A call to a function in the NVIDIA CUDA Runtime library resulted in an error condition. For more detailed information, see the source string of the error cluster containing the error code. |
| −359630 | A call to a function in the NVIDIA CUBLAS library resulted in an error condition. For more detailed information, see the source string of the error cluster containing the error code. |
| −359620 | You attempted to unlock data that is not the same as the data that was previously locked. A typical cause for this error is wiring the output from the wrong Data Value Reference Write Element border node on the border of an In Place Element structure to the unlock function. |
| −359610 | The inputs do not satisfy the dimension requirements for the function. |
| −359601 | You attempted to pass an invalid data reference to the GPU SDK API. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpu/gpu_glossary.html language=enus -->
## TOPIC 00004: Glossary (GPU Analysis Toolkit)

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpu/gpu_glossary.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpu/gpu_glossary.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Glossary (GPU Analysis Toolkit)

ACDF

| A |  |
| --- | --- |
| allocating memory | The process of acquiring a memory buffer on the device to store both the source data that you download to the device and the results of the calculations performed on the device to upload to LabVIEW. For more information about this process, refer to the Performing FFT or BLAS Operations on a GPU Device topic. |
| C |  |
| CUBLAS handle | A pointer that LabVIEW creates when you initialize the CUBLAS library. A handle is a pointer to the master pointer maintained by the memory manager, which updates the pointer if you move the handle to a new address. |
| CUFFT handle | A pointer that LabVIEW creates when you initialize the CUFFT library. A handle is a pointer to the master pointer maintained by the memory manager, which updates the pointer if you move the handle to a new address. |
| D |  |
| data pointer | The physical address of a set of data on the host computer or on the GPU device. See also device data. |
| device data | The cluster of data that contains pointers, data properties, and the raw data from the device. Device data also can refer to the raw data independent of the associated data properties and pointers. |
| device pointer | The physical address of a device resource. A device pointer usually refers to the location of a memory buffer. |
| device pointer class | A LabVIEW class to store device pointer data. |
| device pointer data | Any data that contains a device pointer. |
| F |  |
| freeing memory | The process of releasing the memory buffer on the device that stores the device data. Refer to the Free Memory VI for more information about releasing allocated memory. To end most GPU applications, you must release the memory you allocate on the device, free the initialized resources, such as the CUFFT or CUBLAS library, and free the resources for communication with a device and for active processes. For more information about this workflow, refer to the Designing the Block Diagram to Compute on a GPU Device topic. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpu/lvgpu.html language=enus -->
## TOPIC 00005: GPU Analysis Toolkit

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpu/lvgpu.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpu/lvgpu.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### GPU Analysis Toolkit

June 2012, 373575A-01

The LabVIEW GPU Analysis Toolkit is a software package that allows you to write a LabVIEW application that [offloads FFT or BLAS operations](../lvgpu/computing_operations_on_gpu.html) to a graphics processing unit (GPU). The toolkit is designed to offload operations with data sets large enough to exceed CPU capabilities or operations with significant amounts of parallel computations. To use the GPU Analysis Toolkit, you must have a GPU hardware device installed where it is accessible from the host processor.

#### Communication between LabVIEW and a GPU

The GPU Analysis Toolkit uses a software development kit called the [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html). The LVGPU SDK creates a special execution environment, or context, in which to perform operations on a GPU. It communicates with a GPU [through an API](/csh?topicname=lvexcodeconcepts/calling_external_apis.html), which is responsible for managing GPU execution from the host. In this toolkit, the function wrappers for the FFT and BLAS operations already are built with the LVGPU SDK, and they specifically call the NVIDIA CUDA libraries and communicate with a GPU through an NVIDIA API. You can use the LVGPU SDK to build wrappers for implementing custom GPU functions to execute on any co-processor device as long as LabVIEW can call the external function.

To comment on National Instruments documentation, refer to the National Instruments website.

© 2012 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_create_ctxt.html language=enus -->
## TOPIC 00006: Create Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_create_ctxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_create_ctxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Generates a device context, or special execution environment, in which to perform operations on the device.

You must call the [Initialize Device](../lvgpuvi/gpu_initialize_device.html) VI or the [Initialize Library](../lvgpuvi/api_ini_lib.html) VI before calling this VI to create a [context](../lvgpu/lvgpu.html).

[Details](#details)

[IMAGE alt='image' src='create_context.gif']

|  | CUDA Device specifies the device that owns the context. |
| --- | --- |
|  | flags specifies the context properties. 0CU_CTX_SCHED_AUTO (default)1CU_CTX_MAP_HOST |
| 0 | CU_CTX_SCHED_AUTO (default) |
| 1 | CU_CTX_MAP_HOST |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Context Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_destroy_cntxt.html language=enus -->
## TOPIC 00007: Destroy Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_destroy_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_destroy_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Destroy Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Closes the device context. This VI halts all computations in the context and frees any resources allocated to the context.

[Details](#details)

[IMAGE alt='image' src='destroy_context.gif']

|  | CUDA Context specifies the device context to close. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Destroy Context Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_get_cntxt.html language=enus -->
## TOPIC 00008: Get Current Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_get_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_get_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Current Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Retrieves the current, active device context.

[Details](#details)

[IMAGE alt='image' src='get_current_context.gif']

|  | CUDA Context in specifies the device context that stores the result. |
| --- | --- |
|  | Is Primary? specify TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the current, active device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Current Context Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_get_dr_version.html language=enus -->
## TOPIC 00009: Get CUDA Driver API Version VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_get_dr_version.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_get_dr_version.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get CUDA Driver API Version VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Returns the version information for the CUDA driver API. The active NVIDIA display driver for the host operating system determines the **CUDA Driver version**.

[Details](#details)

[IMAGE alt='image' src='get_cuda_driver_api_version.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUDA Driver version returns the CUDA Driver API version running on the host system. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get CUDA Driver API Version Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_get_runver.html language=enus -->
## TOPIC 00010: Get CUDA Runtime API Version VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_get_runver.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_get_runver.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get CUDA Runtime API Version VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Returns the version information for the device context.

The context version information is unique and may not be the same as the [CUDA Driver API Version](api_get_dr_version.html) VI.

[Details](#details)

[IMAGE alt='image' src='get_cuda_runtime_api_version.gif']

|  | CUDA Context in specifies the device context to inspect. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the inspected device context. |
|  | CUDA Runtime API version returns the CUDA Runtime API that creates the device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get CUDA Runtime API Version Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_ini_lib.html language=enus -->
## TOPIC 00011: Initialize Library VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_ini_lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_ini_lib.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Library VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Prepares a CUDA driver API to call from LabVIEW.

[Details](#details)

[IMAGE alt='image' src='initialize_library_api.gif']

|  | flags specifies special properties for execution in a CUDA context. |
| --- | --- |
|  | Select CUDA Runtime Version specifies the method you select to determine the version of CUDA to use at run time. 0Default—On Windows, Default selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer.1By Environment—Selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer.2By Path—Selects the CUDA version by examining the path you provide in the CUDA Runtime Version Info input to where the CUDA libraries are installed. |
| 0 | Default—On Windows, Default selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer. |
| 1 | By Environment—Selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer. |
| 2 | By Path—Selects the CUDA version by examining the path you provide in the CUDA Runtime Version Info input to where the CUDA libraries are installed. |
|  | CUDA Runtime Version Info specifies additional information based on Select CUDA Runtime Version. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Version returns the current CUDA version based on the method you select in the Select CUDA Runtime Version input. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Library Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_pop_cntxt.html language=enus -->
## TOPIC 00012: Pop Current Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_pop_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_pop_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Pop Current Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Sets the previous device context if one exists.

[Details](#details)

[IMAGE alt='image' src='pop_current_context.gif']

|  | CUDA Context in specifies the device context to deactivate, or pop. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the deactivated device context. |
|  | CUcontext returns the previous, active CUDA context handle. |
|  | Is Primary? returns TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Pop Current Context Details

This VI is equivalent to the [Synchronize Context](../lvgpuvi/api_sync_cntxt.html) VI when the **CUDA Context in** input references a primary context created by the [Initialize Device](../lvgpuvi/gpu_initialize_device.html) VI.

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_push_cntxt.html language=enus -->
## TOPIC 00013: Push Current Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_push_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_push_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Push Current Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Sets the current, active device context.

If you call the [Pop Current Context](../lvgpuvi/api_pop_cntxt.html) VI after calling this VI, the previous, active context becomes the current context.

|  | Note You must call the Push Current Context VI from another VI that has subroutine priority set from the Execution page of VI Properties dialog box. |
| --- | --- |

[Details](#details)

[IMAGE alt='image' src='push_current_context.gif']

|  | CUDA Context in specifies the device context to push. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the current, active device context. |
|  | CUcontext returns the previous, active CUDA context handle. |
|  | Is Primary? returns TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Push Current Context Details

This VI is equivalent to the [Set Current Context](../lvgpuvi/api_set_cntxt.html) VI when the **CUDA Context in** input references a primary context created by the [Initialize Device](../lvgpuvi/gpu_initialize_device.html) VI.

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_set_cntxt.html language=enus -->
## TOPIC 00014: Set Current Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_set_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_set_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Current Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Assigns the current, active device context that replaces the previous, active context.

|  | Note You must call the Set Current Context VI from another VI that has subroutine priority set from the Execution page of VI Properties dialog box. |
| --- | --- |

[Details](#details)

[IMAGE alt='image' src='set_current_context.gif']

|  | CUDA Context in specifies the device context to set. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the current, active device context. |
|  | Is Primary? returns TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Current Context Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/api_sync_cntxt.html language=enus -->
## TOPIC 00015: Synchronize Context VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/api_sync_cntxt.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/api_sync_cntxt.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Synchronize Context VI

**Owning Palette:** [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html)

**Requires:** GPU Analysis Toolkit

Waits for all operations running in the device context to finish. If any operation fails during synchronization, this VI returns an error.

This VI provides the underlying call for the [Synchronize Device](../lvgpuvi/gpu_sync_context.html) VI on the [LVCUDA](../lvgpuvi/lvcuda_pal.html) palette.

[Details](#details)

[IMAGE alt='image' src='synchronize_context.gif']

|  | CUDA Context in specifies the device context to synchronize. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the synchronized device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Synchronize Context Details

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_alloc_mem.html language=enus -->
## TOPIC 00016: Allocate Memory VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_alloc_mem.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_alloc_mem.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Allocate Memory VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Acquires memory, in the form of a buffer, from the device.

You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='allocate_memory.gif']

|  | CUDA Context in specifies the device context in which to allocate memory. |
| --- | --- |
|  | size in elements specifies the number of elements to allocate. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context with allocated memory. |
|  | CUDA U8 Device Ptr returns a class with access to the allocated memory. For example, wire this output to the dst in input on the Download Data VI to supply the allocated memory for the elements to update on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Allocate Memory Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Allocate Memory VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_copy_data.html language=enus -->
## TOPIC 00017: Copy Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_copy_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_copy_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Copy Data VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Transfers copies of data between arrays in memory blocks on the device. If the array you want to copy and the device memory store different amounts of data, this VI limits the transfer to the smaller of the two amounts.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='copy_data.gif']

|  | src in specifies the source elements in an array on the device. |
| --- | --- |
|  | dst in specifies the updated elements in an array on the device. |
|  | count in elements specifies the number of elements to copy. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | src out returns the source elements in an array on the device. |
|  | dst out returns the updated elements in an array on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Copy Data Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Copy Data VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_create_array.html language=enus -->
## TOPIC 00018: Create Array Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_create_array.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_create_array.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Array Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Generates a class to store and manage 1D array data.

You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='create_array_data.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | GPU 1D U8 Array Data returns the class that manages a 1D array data pointer. This output returns a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_create_custom.html language=enus -->
## TOPIC 00019: Create Custom Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_create_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_create_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Custom Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Creates a class that stores and manages custom data.

You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[IMAGE alt='image' src='create_custom_data.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | GPU Custom Data returns the class that manages custom data. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_create_data.html language=enus -->
## TOPIC 00020: Create Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_create_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_create_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Data VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Generates a class that stores and manages device property data, including a device memory resource and a device context. This VI also can generate a class to manage other data associated with the device, such as the execution of functions from the CUFFT library and the CUBLAS library on the device.

You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

#### Create Data (Device Ptr:U8)

The connector pane displays the default data types for the Device Ptr instance of this polymorphic function.

[IMAGE alt='image' src='create_data.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUDA U8 Device Ptr returns the class managing a CUDA device pointer of type CUdeviceptr. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | CUBLAS Handle returns the class managing a CUBLAS handle of type cublasHandle. |

#### Create Data (Context)

[IMAGE alt='image' src='create_cuda_context.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUDA Context returns the class managing a CUDA context of type CUcontext. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | CUBLAS Handle returns the class managing a CUBLAS handle of type cublasHandle. |

#### Create Data (CUFFT Handle)

[IMAGE alt='image' src='create_cufft_handle.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUFFT Handle returns the class managing a CUFFT handle of type cufftHandle. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | CUBLAS Handle returns the class managing a CUBLAS handle of type cublasHandle. |

#### Create Data (CUBLAS Handle)

[IMAGE alt='image' src='create_cublas_handle.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUBLAS Handle returns the class managing a CUBLAS handle of type cublasHandle. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | CUBLAS Handle returns the class managing a CUBLAS handle of type cublasHandle. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_data_unlock.html language=enus -->
## TOPIC 00021: Prepare Data For Unlock VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_data_unlock.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_data_unlock.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Prepare Data For Unlock VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Begins the process of unlocking device data. Use this VI as the last step in protecting the device data from modification or deletion while in use. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)

[IMAGE alt='image' src='prepare_cuda_device_ptr_for_unlock.gif']

|  | CUDA U8 Device Ptr in specifies a device pointer class with locked data. This input also accepts a CUDA context, a CUFFT handle, or a CUBLAS handle with locked data. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | CUDA U8 Device Ptr Data Reference specifies the device pointer, CUDA context, CUFFT handle, or CUBLAS handle data value reference to unlock. |
|  | CUDA Context specifies the device context class in which the device pointer, the CUFFT handle, or the CUBLAS handle were created. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns a device pointer class, CUDA context class, CUFFT handle class, or a CUBLAS handle class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Prepare Data For Unlock Details

The outputs from the [Prepare Data For Lock](../lvgpuvi/gpu_lock_data.html) VI provide the inputs for this VI. Refer to the [Details](../lvgpuvi/gpu_lock_data.html#details) section of the Prepare Data For Lock VI for more information about the locking and unlocking [device data](../lvgpu/gpu_glossary.html#d) process.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_dest_data.html language=enus -->
## TOPIC 00022: Destroy Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_dest_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_dest_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Destroy Data VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Closes the class that stores and manages device data, as well as the underlying device data. When the device data controls execution or resources, this VI may halt certain functions or free resources. Wire data to the **CUDA U8 Device Ptr** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='destroy_data.gif']

|  | CUDA U8 Device Ptr specifies a device pointer class to free, a CUDA context to destroy, a CUFFT handle release, or a CUBLAS handle to release based on the data type you wire to this input. If you wire a CUDA device pointer to this input, it can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_destroy_array.html language=enus -->
## TOPIC 00023: Destroy Array Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_destroy_array.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_destroy_array.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Destroy Array Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Closes a class that stores and manages 1D array data. If the class has the cleanup procedure address property set, this VI calls the cleanup procedure based on the procedure address stored in the property. Wire data to the **GPU 1D U8 Array Data** input to determine the polymorphic instance to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='destroy_array_data.gif']

|  | GPU 1D U8 Array Data specifies a 1D array data pointer class. This input accepts a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_destroy_custom.html language=enus -->
## TOPIC 00024: Destroy Custom Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_destroy_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_destroy_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Destroy Custom Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Closes a class that stores and manages custom data. If the class has the cleanup procedure address property set, this VI calls the cleanup procedure based on the procedure address stored in the property.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[IMAGE alt='image' src='destroy_custom_data.gif']

|  | GPU Custom Data specifies the class managing custom data. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_device_prop.html language=enus -->
## TOPIC 00025: Get Device Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_device_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_device_prop.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Device Properties VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the properties for a device using the device ID you provide. Device properties can include such properties as the device name, the amount of memory, the number of threads, and the device version.

[Details](#details)

[IMAGE alt='image' src='get_device_properties.gif']

|  | device specifies the device ID of the device to inspect. |
| --- | --- |
|  | max name length specifies the maximum character length for the device name. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Device Properties returns a collection of device properties. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Device Properties Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_down_data.html language=enus -->
## TOPIC 00026: Download Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_down_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_down_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Download Data VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Transfers data from a 1D or 2D array to memory, in the form of a buffer, on the device. If the array and the memory on the device store different amounts of data, this VI limits the transfer to the smaller of the two amounts. Wire data to the **src in** or **dst in** input to determine the polymorphic instance to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='download_1d_data.gif']

|  | src in specifies the source elements to download to the device. src in accepts a 1D or 2D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point numbers |
| --- | --- |
|  | dst in specifies the allocated memory for the elements to update on the device. For example, you can wire the device pointer output from the Allocate Memory VI to this input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | src out returns the source elements stored in a 1D or 2D array. |
|  | dst out returns the updated elements in an array on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Download Data Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Download Data VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_fft_vi.html language=enus -->
## TOPIC 00027: FFT VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_fft_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_fft_vi.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FFT VI

**Owning Palette:** [LVCUFFT](../lvgpuvi/lvcufft_pal.html)

**Requires:** GPU Analysis Toolkit

Computes the fast Fourier transform of signals and returns the spectrums. Wire data to the **signals in** input to determine the polymorphic instance or you can manually select which instance to use.

[Details](#details)  [Example](#examples)

#### Real FFT (SGL (Inplace))

[IMAGE alt='image' src='real_fft_(sgl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Real FFT (DBL (Inplace))

[IMAGE alt='image' src='real_fft_(dbl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Real FFT (SGL->CSG)

When you leave **spectrums in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='real_fft_(sgl_csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the memory, in the form of a buffer, on the device to store the results of the FFT calculation. |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | signals out returns the unchanged elements you wire to signals in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Real FFT (DBL->CDB)

When you leave **spectrums in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='real_fft_(dbl_cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the memory, in the form of a buffer, on the device to store the results of the FFT calculation. |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | signals out returns the unchanged elements you wire to signals in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Real FFT (CSG (Inplace))

[IMAGE alt='image' src='real_fft_(csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Real FFT (CDB (Inplace))

[IMAGE alt='image' src='real_fft_(cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Complex FFT (CSG (Inplace))

[IMAGE alt='image' src='complex_fft_(csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Complex FFT (CSG->CSG)

When you leave **spectrums in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='complex_fft_(csg_csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the memory, in the form of a buffer, on the device to store the results of the FFT calculation. |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | signals out returns the unchanged elements you wire to signals in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Complex FFT (CDB (Inplace))

[IMAGE alt='image' src='complex_fft_(cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Complex FFT (CDB->CDB)

When you leave **spectrums in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='complex_fft_(cdb_cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the memory, in the form of a buffer, on the device to store the results of the FFT calculation. |
|  | signals in specifies the input signals. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle to the initialized CUFFT library. |
|  | spectrums out returns the output spectrums from the FFT operation. |
|  | signals out returns the unchanged elements you wire to signals in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### FFT Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUFFT library and FFT operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUFFT Library User Guide.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the FFT VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_free_mem.html language=enus -->
## TOPIC 00028: Free Memory VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_free_mem.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_free_mem.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Free Memory VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Releases the memory, or buffer, on the device that stores data. Wire data to the **CUDA U8 Device Ptr** input to determine the polymorphic instance to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='free_memory.gif']

|  | CUDA U8 Device Ptr specifies a class with access to allocated memory. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Free Memory Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Free Memory VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_array_prop.html language=enus -->
## TOPIC 00029: Get Array Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_array_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_array_prop.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Array Data Properties VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the 1D array data properties and extra data elements in the 1D array data class. Wire data to the **GPU 1D U8 Array Data in** input to determine the polymorphic instance to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)

[IMAGE alt='image' src='get_array_data_properties.gif']

|  | GPU 1D U8 Array Data in specifies a 1D array data pointer class. This input accepts a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Extra Data Dim returns the size, in elements, of the 1D array data. |
|  | Extra Data Ptr returns the extra data pointer stored in addition to the 1D array data. |
|  | GPU 1D U8 Array Data out returns the 1D array data pointer class. This output returns the same data type that you wire to GPU 1D U8 Array Data in. |
|  | GPU Array Descriptor returns the 1D array data properties. |
|  | Extra Custom Data returns an extra GPU custom data class stored in the 1D array data class. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Cleanup Procedure Address returns the address of the procedure that releases the 1D array data and the extra data pointer. |

#### Get Array Data Properties Details

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_custom.html language=enus -->
## TOPIC 00030: Get Custom Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Custom Data Properties VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the extra data properties stored in the custom data class.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[IMAGE alt='image' src='get_custom_data_properties.gif']

|  | GPU Custom Data in specifies a custom data class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GPU Custom Data out returns a custom data class. |
|  | Extra Data Ptr returns the extra data pointer. |
|  | Extra Custom Data returns an extra GPU custom data class. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Cleanup Procedure Address returns the address of the procedure that frees the extra data pointer. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_device.html language=enus -->
## TOPIC 00031: Get Device VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_device.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_device.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Device VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the device ID for the device context you provide.

[Details](#details)

[IMAGE alt='image' src='get_device.gif']

|  | CUDA Context in specifies the device context to inspect. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the inspected device context. |
|  | CUDA Device returns the device ID associated with the device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Device Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_prop.html language=enus -->
## TOPIC 00032: Get Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_prop.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Data Properties VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the raw device data and properties in the device data class. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[Details](#details)

#### Get Data Properties (Device Ptr:U8)

The connector pane displays the default data types for the Device Ptr instance of this polymorphic function.

[IMAGE alt='image' src='get_data_properties.gif']

|  | CUDA U8 Device Ptr in specifies a device pointer class. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context returns the device context class that creates the device pointer. |
|  | CUDA U8 Device Ptr out returns the device pointer class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | U8 * returns the device pointer. This input can return the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
|  | dim returns the number of elements the device pointer allocates. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Data Properties (CUDA Context)

[IMAGE alt='image' src='get_cuda_context_properties.gif']

|  | CUDA Context in specifies a device context class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context class. |
|  | CUcontext returns the CUDA context. |
|  | Is Primary? returns TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Data Properties (CUFFT Handle)

[IMAGE alt='image' src='get_cufft_handle_properties.gif']

|  | CUFFT Handle in specifies a CUFFT handle class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the CUFFT handle class. |
|  | cufftHandle returns the CUFFT handle. |
|  | CUDA Context returns the device context class in which the CUFFT handle was created. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Data Properties (CUBLAS Handle)

[IMAGE alt='image' src='get_cublas_handle_properties.gif']

|  | CUBLAS Handle in specifies a CUBLAS handle class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUBLAS Handle out returns a CUBLAS handle class. |
|  | cublasHandle_t returns the CUBLAS handle. |
|  | CUDA Context returns the device context class in which the CUBLAS handle was created. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Data Properties Details

The [data value reference](/csh?topicname=lvconcepts/external_data_val_ref.html) returned in the **CUDA U8 Device Ptr out**, **CUDA Context out**, **CUFFT Handle out**, or **CUBLAS Handle out** output stores the [device data](../lvgpu/gpu_glossary.html#d). Wire this output to a [Data Value Reference Read / Write Element](/csh?topicname=glang/inplace_datareference.html) border node on an [In Place Element](/csh?topicname=glang/in_place_element_structure.html) structure, which locks the data value reference while you operate on the code inside the In Place Element structure. To unlock the device data, wire it to the Data Value Reference Write Element node. You can make the device data available to other processes by wiring the output of the Data Value Reference Write Element node to the [Prepare Data for Unlock](../lvgpuvi/gpu_data_unlock.html) VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_vers_blas.html language=enus -->
## TOPIC 00033: Get Version VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_vers_blas.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_vers_blas.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Version VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Returns the version information for the CUBLAS library.

[IMAGE alt='image' src='get_version_lvcublas.gif']

|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. This input also determines the device that executes the function. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | CUBLAS version returns the current version of the initialized CUBLAS library. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_vers_fft.html language=enus -->
## TOPIC 00034: Get Version VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_vers_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_vers_fft.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Version VI

**Owning Palette:** [LVCUFFT](../lvgpuvi/lvcufft_pal.html)

**Requires:** GPU Analysis Toolkit

Returns the version information for the CUFFT library.

[IMAGE alt='image' src='get_version_lvcufft.gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the FFT calculation. This input also determines the device executing the function. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | CUFFT version returns the current version of the initialized CUFFT library. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_get_version.html language=enus -->
## TOPIC 00035: Get Version Information VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_get_version.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_get_version.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Version Information VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Returns the version information for the CUDA Runtime API, the CUDA Driver API, and the CUDA Toolkit that built the GPU Analysis Toolkit.

[Details](#details)

[IMAGE alt='image' src='get_version_information.gif']

|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
| --- | --- |
|  | CUDA Build version returns the CUDA Toolkit version that builds the GPU Analysis Toolkit. |
|  | CUDA Driver version returns the CUDA Driver API version running on the host system. |
|  | CUDA Runtime version returns the version of the CUDA Runtime API that the GPU Analysis Toolkit uses when calling the Initialize Device VI or the Create Context VI with default parameters. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Version Information Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_ini_fft_lib.html language=enus -->
## TOPIC 00036: Initialize Library VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_ini_fft_lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_ini_fft_lib.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Library VI

**Owning Palette:** [LVCUFFT](../lvgpuvi/lvcufft_pal.html)

**Requires:** GPU Analysis Toolkit

Prepares the device for FFT operations by selecting the type of FFT you want to compute. The initialization process reserves resources on the device to improve performance.

You must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)  [Example](#examples)

#### Initalize Library (1D FFT)

[IMAGE alt='image' src='create_1d_fft_plan.gif']

|  | CUDA Context in specifies the device context in which to initialize the CUFFT library. |
| --- | --- |
|  | size specifies the size of the signals to transform. |
|  | type specifies the type of FFT to compute. The FFT type includes information on the FFT size, the number of FFTs to perform in parallel on the device, and the data type of the input signals or spectrums. 0CUFFT_R2C—Real FFT – SGL1CUFFT_C2R—Inverse Real FFT – SGL2CUFFT_C2C (default)—(Inverse) Complex FFT - CSG3CUFFT_D2Z—Real FFT – DBL4CUFFT_Z2D—Inverse Real FFT – DBL5CUFFT_Z2Z—(Inverse) Complex FFT – CDB |
| 0 | CUFFT_R2C—Real FFT – SGL |
| 1 | CUFFT_C2R—Inverse Real FFT – SGL |
| 2 | CUFFT_C2C (default)—(Inverse) Complex FFT - CSG |
| 3 | CUFFT_D2Z—Real FFT – DBL |
| 4 | CUFFT_Z2D—Inverse Real FFT – DBL |
| 5 | CUFFT_Z2Z—(Inverse) Complex FFT – CDB |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | batch specifies the number of signals to transform. |
|  | CUDA Context out returns the device context in which LabVIEW initializes the FFT library. |
|  | CUFFT Handle returns the handle to the FFT library. |
|  | CUFFT Version returns the current version of the initialized CUFFT library. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initalize Library (2D FFT)

[IMAGE alt='image' src='create_2d_fft_plan.gif']

|  | CUDA Context in specifies the device context in which to initialize the CUFFT library. |
| --- | --- |
|  | rows specifies the size, in rows, of the signals to transform. |
|  | columns specifies the size, in columns, of the signals to transform. |
|  | type specifies the type of FFT to compute. The FFT type includes information on the FFT size, the number of FFTs to perform in parallel on the device, and the data type of the input signals or spectrums. 0CUFFT_R2C—Real FFT – SGL1CUFFT_C2R—Inverse Real FFT – SGL2CUFFT_C2C (default)—(Inverse) Complex FFT - CSG3CUFFT_D2Z—Real FFT – DBL4CUFFT_Z2D—Inverse Real FFT – DBL5CUFFT_Z2Z—(Inverse) Complex FFT – CDB |
| 0 | CUFFT_R2C—Real FFT – SGL |
| 1 | CUFFT_C2R—Inverse Real FFT – SGL |
| 2 | CUFFT_C2C (default)—(Inverse) Complex FFT - CSG |
| 3 | CUFFT_D2Z—Real FFT – DBL |
| 4 | CUFFT_Z2D—Inverse Real FFT – DBL |
| 5 | CUFFT_Z2Z—(Inverse) Complex FFT – CDB |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | batch specifies the number of signals to transform. |
|  | CUDA Context out returns the device context in which LabVIEW initializes the FFT library. |
|  | CUFFT Handle returns the handle to the FFT library. |
|  | CUFFT Version returns the current version of the initialized CUFFT library. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Library Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Initialize Library VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_ini_lib_blas.html language=enus -->
## TOPIC 00037: Initialize Library VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_ini_lib_blas.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_ini_lib_blas.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Library VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Prepares the device for CUBLAS operations by providing a handle to the CUBLAS library for use in LabVIEW.

[Details](#details)

[IMAGE alt='image' src='initialize_library_lvcublas.gif']

|  | CUDA Context in specifies the device context in which to initialize the CUBLAS library. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context in which LabVIEW initializes the CUBLAS library. |
|  | CUBLAS Handle returns the handle to the initialized CUBLAS library. |
|  | CUBLAS Version returns the current version of the initialized CUBLAS library. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Library Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_ini_memory.html language=enus -->
## TOPIC 00038: Initialize Memory VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_ini_memory.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_ini_memory.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Memory VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Sets each byte of each element in memory on the device. This VI sets each byte up to the number of elements provided.

you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)

[IMAGE alt='image' src='initialize_memory.gif']

|  | CUDA U8 Device Ptr in specifies a class with access to allocated memory on the device. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | byte value specifies the initialization value. The default is 0. |
|  | elements specifies the number of elements to initialize. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns a class with access to initialized memory. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Memory Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_initialize_device.html language=enus -->
## TOPIC 00039: Initialize Device VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_initialize_device.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_initialize_device.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Device VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Creates the special execution environment, or context, necessary for LabVIEW to communicate with the GPU.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='initialize_device.gif']

|  | CUDA Device ID specifies the device ID of the NVIDIA GPU. The default is 0. |
| --- | --- |
|  | Select CUDA Runtime Version specifies the method you select to determine the version of CUDA to use at run time. 0Default—On Windows, Default selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer.1By Environment—Selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer.2By Path—Selects the CUDA version by examining the path you provide in the CUDA Runtime Version Info input to where the CUDA libraries are installed. |
| 0 | Default—On Windows, Default selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer. |
| 1 | By Environment—Selects the CUDA version by examining the environment variable for the path containing the bin folder where the CUDA libraries are installed on the host computer. |
| 2 | By Path—Selects the CUDA version by examining the path you provide in the CUDA Runtime Version Info input to where the CUDA libraries are installed. |
|  | CUDA Runtime Version Info specifies additional information based on Select CUDA Runtime Version. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context that manages device execution and device resources. |
|  | CUDA Version returns the current CUDA version based on the method you select in the Select CUDA Runtime Version input. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Device Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Initialize Device VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_inverse_fft.html language=enus -->
## TOPIC 00040: Inverse FFT VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_inverse_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_inverse_fft.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse FFT VI

**Owning Palette:** [LVCUFFT](../lvgpuvi/lvcufft_pal.html)

**Requires:** GPU Analysis Toolkit

Computes the inverse fast Fourier transform of spectrums and returns the signals. Wire data to the **spectrums in** input to determine the polymorphic instance or you can manually select which instance to use.

[Details](#details)

#### Inverse Real FFT (SGL (Inplace))

[IMAGE alt='image' src='inverse_real_fft_(sgl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Real FFT (CSG->SGL)

When you leave **signals in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='inverse_real_fft_(csg_sgl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the memory, in the form of a buffer, on the device where you want to store the result of the inverse FFT calculation. |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | spectrums out returns the unchanged elements you wire to spectrums in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Real FFT (DBL (Inplace))

[IMAGE alt='image' src='inverse_real_fft_(dbl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Real FFT (CDB->DBL)

When you leave **signals in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='inverse_real_fft_(cdb_dbl).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | signals in specifies the memory, in the form of a buffer, on the device where you want to store the result of the inverse FFT calculation. |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | spectrums out returns the unchanged elements you wire to spectrums in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Real FFT (CSG (Inplace))

[IMAGE alt='image' src='inverse_real_fft_(csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Real FFT (CDB (Inplace))

[IMAGE alt='image' src='inverse_real_fft_(cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Complex FFT (CSG (Inplace))

[IMAGE alt='image' src='inverse_complex_fft_(csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Complex FFT (CSG->CSG)

When you leave **signals in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='inverse_complex_fft_(csg_csg).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | signals in specifies the memory, in the form of a buffer, on the device where you want to store the result of the inverse FFT calculation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | spectrums out returns the unchanged elements you wire to spectrums in. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Complex FFT (CDB (Inplace))

[IMAGE alt='image' src='inverse_complex_fft_(cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Complex FFT (CDB->CDB)

When you leave **signals in** unwired, this VI performs the operation inplace.

[IMAGE alt='image' src='inverse_complex_fft_(cdb_cdb).gif']

|  | CUFFT Handle in specifies the initialized CUFFT library to use for the inverse FFT calculation. For example, you can wire the CUFFT Handle output from the Initialize Library VI to specify the CUFFT handle to the CUFFT library you already initialized. This input also determines the device that executes the function. |
| --- | --- |
|  | spectrums in specifies the input spectrums. For example, you can wire the dst out output from the Download Data VI to this input to specify the elements on the device that you want to compute. |
|  | signals in specifies the memory, in the form of a buffer, on the device where you want to store the result of the inverse FFT calculation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the handle that defines the inverse FFT operation. |
|  | spectrums out returns the unchanged elements you wire to spectrums in. |
|  | signals out returns the output signals from the inverse FFT operation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse FFT Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUFFT library and inverse FFT operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUFFT Library User Guide.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_lock_data.html language=enus -->
## TOPIC 00041: Prepare Data For Lock VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_lock_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_lock_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Prepare Data For Lock VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Begins the process of locking device data.

Use this VI as the first step in [protecting the device data](gpu_lock_data.html#details) from modification or deletion while in use. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)

[IMAGE alt='image' src='prepare_cuda_device_ptr_for_lock.gif']

|  | CUDA U8 Device Ptr in specifies a device pointer class. This input also accepts a CUDA context class, a CUFFT handle class, or a CUBLAS handle class. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns a device pointer class, CUDA context class, CUFFT handle class, or a CUBLAS handle class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | CUDA U8 Device Ptr Data Reference returns the device pointer, CUDA context, CUFFT handle, or CUBLAS handle reference to lock. This output returns a data value reference to a class with the same data type that you wire to CUDA U8 Device Ptr in. |
|  | CUDA Context returns the device context class in which the device pointer, the CUFFT handle, or the CUBLAS handle was created. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Prepare Data For Lock Details

The [device data](../lvgpu/gpu_glossary.html#d) is stored using a [data value reference](/csh?topicname=lvconcepts/external_data_val_ref.html) returned in the **CUDA Device Ptr out**, **CUDA Context out**, **CUFFT Handle out**, or **CUBLAS Handle out** output. Wire this output to a [Data Value Reference Read Element](/csh?topicname=glang/inplace_datareference.html) border node on an [In Place Element](/csh?topicname=glang/in_place_element_structure.html) structure, which locks the [data value reference](/csh?topicname=lvconcepts/external_data_val_ref.html) while you operate on the code inside the In Place Element structure. To unlock the device data, wire it to the Data Value Reference Write Element node. You can make the device data available to other processes by wiring the output of the Data Value Reference Write Element node to the [Prepare Data for Unlock VI](../lvgpuvi/gpu_data_unlock.html).

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_read_array.html language=enus -->
## TOPIC 00042: Read Array Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_read_array.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_read_array.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read Array Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the member data from a 1D array data class. Wire data to the **GPU 1D U8 Array Data in** input to determine the polymorphic instance to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='read_array_data.gif']

|  | GPU 1D U8 Array Data in specifies a 1D array data pointer class. This input accepts a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GPU 1D U8 Array Data out returns the 1D array data pointer class. This output returns the same data type that you wire to GPU 1D U8 Array Data in. |
|  | 1D U8 Array Data Reference returns the device pointer reference. This output returns a data value reference with the same data type that you wire to GPU 1D U8 Array Data in. |
|  | dim returns the size, in elements, of the 1D array data. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_read_custom.html language=enus -->
## TOPIC 00043: Read Custom Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_read_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_read_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read Custom Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the member data from a custom data class.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[IMAGE alt='image' src='read_custom_data.gif']

|  | GPU Custom Data in specifies a custom data class. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GPU Custom Data out returns a custom data class. |
|  | Custom Data Reference returns the data data value reference containing the custom data properties. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_read_data.html language=enus -->
## TOPIC 00044: Read Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_read_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_read_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read Data VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Retrieves the member data from a device data class. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='read_data.gif']

|  | CUDA U8 Device Ptr in specifies a device pointer class. This input also accepts a CUDA context class, a CUFFT handle class, or a CUBLAS handle class. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns a device pointer class, CUDA context class, CUFFT handle class, or a CUBLAS handle class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | CUDA U8 Device Ptr Data returns the class data for the class you wire to CUDA U8 Device Ptr in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_rel_lib_blas.html language=enus -->
## TOPIC 00045: Release Library VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_rel_lib_blas.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_rel_lib_blas.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Release Library VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Frees the initialized CUBLAS library by halting any BLAS computations in process and freeing any resources allocated during initialization for BLAS computations.

[Details](#details)

[IMAGE alt='image' src='release_library_lvcublas.gif']

|  | CUBLAS Handle specifies the handle to the CUBLAS library to free. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Release Library Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_release_dev.html language=enus -->
## TOPIC 00046: Release Device VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_release_dev.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_release_dev.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Release Device VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Frees the device context and any resources allocated since initialization, including resources for communication with the device and any active processes on the device that began after initialization. This VI halts all computations in the context.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='release_device.gif']

|  | CUDA Context specifies the device context to release. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Release Device Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Release Device VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_release_lib.html language=enus -->
## TOPIC 00047: Release Library VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_release_lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_release_lib.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Release Library VI

**Owning Palette:** [LVCUFFT](../lvgpuvi/lvcufft_pal.html)

**Requires:** GPU Analysis Toolkit

Frees the initialized CUFFT library by halting any FFT computations in process and freeing any resources allocated since initialization for FFT computations.

[Details](#details)

[IMAGE alt='image' src='release_library_cufft.gif']

|  | CUFFT Handle in specifies the handle to the CUFFT library to free. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Release Library Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_sdk_pal.html language=enus -->
## TOPIC 00048: LVGPU SDK

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_sdk_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_sdk_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVGPU SDK

**Owning Palette:** [GPU Analysis VIs](../lvgpuvi/lvgpuvi.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the LVGPU SDK VIs to call custom GPU VIs from a LabVIEW application.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Create Array Data | Generates a class to store and manage 1D array data. |
| Create Custom Data | Creates a class that stores and manages custom data. |
| Destroy Array Data | Closes a class that stores and manages 1D array data. If the class has the cleanup procedure address property set, this VI calls the cleanup procedure based on the procedure address stored in the property. Wire data to the GPU 1D U8 Array Data input to determine the polymorphic instance to use. |
| Destroy Custom Data | Closes a class that stores and manages custom data. If the class has the cleanup procedure address property set, this VI calls the cleanup procedure based on the procedure address stored in the property. |
| Get Array Data Properties | Retrieves the 1D array data properties and extra data elements in the 1D array data class. Wire data to the GPU 1D U8 Array Data in input to determine the polymorphic instance to use. |
| Get Custom Data Properties | Retrieves the extra data properties stored in the custom data class. |
| Read Array Data | Retrieves the member data from a 1D array data class. Wire data to the GPU 1D U8 Array Data in input to determine the polymorphic instance to use. |
| Read Custom Data | Retrieves the member data from a custom data class. |
| Set Array Data Properties | Assigns the 1D array data properties and custom data elements to store in the 1D array data class. This VI overwrites any existing properties in the 1D array data class. Wire data to the GPU 1D U8 Array Data in input to determine the polymorphic instance to use. |
| Set Custom Data Properties | Assigns the extra data properties stored in the custom data class. This VI overwrites any existing properties in the custom data class. |
| Write Array Data | Assigns the member data to a 1D array data class. Wire data to the GPU 1D U8 Array Data in input to determine the polymorphic instance to use. |
| Write Custom Data | Assigns the member data to a custom data class. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_set_array_prop.html language=enus -->
## TOPIC 00049: Set Array Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_set_array_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_set_array_prop.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Array Data Properties VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the 1D array data properties and custom data elements to store in the 1D array data class. This VI overwrites any existing properties in the 1D array data class. Wire data to the **GPU 1D U8 Array Data in** input to determine the polymorphic instance to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)

[IMAGE alt='image' src='set_array_data_properties.gif']

|  | Extra Data Dim specifies the size, in elements, of the 1D array data. |
| --- | --- |
|  | Extra Data Ptr specifies the extra data pointer. |
|  | GPU 1D U8 Array Data in specifies a 1D array data pointer class. This input accepts a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
|  | GPU Array Descriptor specifies the 1D array data properties. |
|  | Extra Custom Data specifies an extra GPU custom data class. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cleanup Procedure Address specifies the address of the procedure to free the 1D array data and the extra data pointer. |
|  | GPU 1D U8 Array Data out returns the 1D array data pointer class. This output returns the same data type that you wire to GPU 1D U8 Array Data in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Array Data Properties Details

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

To avoid leaking resources, call the [Get Array Data Properties](../lvgpuvi/gpu_get_array_prop.html) VI to retrieve properties that require special handling. Alternatively, close the 1D array data class by calling the [Destroy Array Data](../lvgpuvi/gpu_destroy_array.html) VI and generate a new 1D array data class using the [Create Array Data](../lvgpuvi/gpu_create_array.html) VI before setting properties with this VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_set_custom.html language=enus -->
## TOPIC 00050: Set Custom Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_set_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_set_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Custom Data Properties VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the extra data properties stored in the custom data class. This VI overwrites any existing properties in the custom data class.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[Details](#details)

[IMAGE alt='image' src='set_custom_data_properties.gif']

|  | GPU Custom Data in specifies a custom data class. |
| --- | --- |
|  | Extra Data Ptr specifies the extra data pointer. |
|  | Extra Custom Data specifies an extra GPU custom data class. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cleanup Procedure Address specifies the address of the procedure that frees the extra data pointer. |
|  | GPU Custom Data out returns a custom data class. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Custom Data Properties Details

To avoid leaking resources, call the [Get Custom Data Properties](../lvgpuvi/gpu_get_custom.html) VI to retrieve properties that require special handling. Alternatively, close the custom data class by calling the [Destroy Custom Data](../lvgpuvi/gpu_destroy_custom.html) VI and generate new custom data class using the [Create Custom Data](../lvgpuvi/gpu_create_custom.html) VI before setting properties with this function.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_set_prop.html language=enus -->
## TOPIC 00051: Set Data Properties VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_set_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_set_prop.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Data Properties VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the device data and properties in the device data class. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[Details](#details)

#### Set Data Properties (Device Ptr:U8)

The connector pane displays the default data types for the Device Ptr instance of this polymorphic function.

[IMAGE alt='image' src='set_data_properties.gif']

|  | CUDA Context specifies the device context class to create the device pointer. |
| --- | --- |
|  | CUDA U8 Device Ptr in specifies a device pointer class. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
|  | U8 * specifies the device pointer. |
|  | dim specifies the number of elements the device pointer allocates. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns the device pointer class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Data Properties (Context)

[IMAGE alt='image' src='set_cuda_context_properties.gif']

|  | CUDA Context in specifies a device context class. |
| --- | --- |
|  | CUcontext specifies the CUDA context. |
|  | Is Primary? specify TRUE if the Initialize Device VI creates the context passed to CUcontext. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the device context class. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Data Properties (CUFFT Handle)

[IMAGE alt='image' src='set_cufft_handle_properties.gif']

|  | CUFFT Handle in specifies a CUFFT handle class. |
| --- | --- |
|  | cufftHandle specifies the CUFFT handle. |
|  | CUDA Context specifies the device context class in which the CUFFT handle was created. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUFFT Handle out returns the CUFFT handle class. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Data Properties (CUBLAS Handle)

[IMAGE alt='image' src='set_cublas_handle_properties.gif']

|  | CUBLAS Handle in specifies a CUBLAS handle class. |
| --- | --- |
|  | cublasHandle_t specifies the CUBLAS handle. |
|  | CUDA Context specifies the device context class in which the CUFFT handle was created. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUBLAS Handle out returns a CUBLAS handle class. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Data Properties Details

The [data value reference](/csh?topicname=lvconcepts/external_data_val_ref.html) returned in the **CUDA U8 Device Ptr out**, **CUDA Context out**, **CUFFT Handle out**, or **CUBLAS Handle out** output stores the [device data](../lvgpu/gpu_glossary.html#d). Wire this output to a [Data Value Reference Read Element](/csh?topicname=glang/inplace_datareference.html) border node on an [In Place Element](/csh?topicname=glang/in_place_element_structure.html) structure, which locks the data value reference while you operate on the code inside the In Place Element structure. To unlock the device data, wire it to the Data Value Reference Write Element node. You can make the device data available to other processes by wiring the output of the Data Value Reference Write Element node to the [Prepare Data for Unlock](../lvgpuvi/gpu_data_unlock.html) VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_sync_context.html language=enus -->
## TOPIC 00052: Synchronize Device VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_sync_context.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_sync_context.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Synchronize Device VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Waits for all operations running on the device to finish. If any operation fails during synchronization, this VI returns an error.

This VI accepts a CUDA device pointer, CUDA context, CUFFT handle, CUBLAS handle.

[Details](#details)

[IMAGE alt='image' src='synchronize_device.gif']

|  | CUDA Context in specifies the device context to synchronize. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA Context out returns the synchronized device context. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Synchronize Device Details

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_syrk.html language=enus -->
## TOPIC 00053: xSYRK (Symmetric Matrix Rank-k Update) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_syrk.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_syrk.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xSYRK (Symmetric Matrix Rank-k Update) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates a symmetric rank-k update of a symmetric matrix. When you wire data to **A in** and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xSYRK (Symmetric Matrix Rank-k Update) (aAA' + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyrk_(aaa'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*A'. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A and C. |
|  | k specifies the number of columns to use in matrix A. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda and ldc for A and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAA'+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAA'+bC returns the result of the calculation. For any other elements, aAA'+bC returns the value of the element in C with the same index. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYRK (Symmetric Matrix Rank-k Update) (aA'A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyrk_(aa'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A'*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A and C. |
|  | k specifies the number of columns to use in matrix A'. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda and ldc for A and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aA'A+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aA'A+bC returns the result of the calculation. For any other elements, aA'A+bC returns the value of the element in C with the same index. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYRK (Symmetric Matrix Rank-k Update) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_up_data.html language=enus -->
## TOPIC 00054: Upload Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_up_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_up_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Upload Data VI

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit

Transfers data from memory on the device, in the form of a buffer, to a 1D or 2D LabVIEW array. If the array and the device memory store different amounts of data, this VI limits the transfer to the smaller of the two amounts. Wire data to the **dst in** or **src in** input to determine the polymorphic instance to use.

The connector pane displays the default data types for this polymorphic function.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='upload_data.gif']

|  | dst in specifies the source elements. The array you wire to this input defines how much data to upload. dst in accepts a 1D or 2D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point numbers |
| --- | --- |
|  | src in specifies the allocated memory for the updated elements on the device. For example, you can wire the results output from a VI that performs calculations to this input to specify the allocated memory in which to store the updated elements. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dst out returns the 1D or 2D array of updated destination elements. This output returns the same data type that you wire to dst in. |
|  | src out returns the source elements on the device to a LabVIEW array. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Upload Data Details

For more information about this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUDA API, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUDA API Reference Manual.

#### Example

Refer to the Multi-channel FFT VI in the labview\examples\lvgpu\Multi-channel FFT directory for an example of using the Upload Data VI.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_write_array.html language=enus -->
## TOPIC 00055: Write Array Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_write_array.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_write_array.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Write Array Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the member data to a 1D array data class. Wire data to the **GPU 1D U8 Array Data in** input to determine the polymorphic instance to use.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='write_array_data.gif']

|  | GPU 1D U8 Array Data in specifies a 1D array data pointer class. This input accepts a 1D array of the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | 1D U8 Array Data Reference specifies the data value reference containing the 1D array data properties. This reference contains the same data type that you wire to the GPU 1D U8 Array Data in input. |
|  | dim returns the size, in elements, of the 1D array data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GPU 1D U8 Array Data out returns the 1D array data pointer class. This output returns the same data type that you wire to GPU 1D U8 Array Data in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_write_custom.html language=enus -->
## TOPIC 00056: Write Custom Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_write_custom.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_write_custom.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Write Custom Data VI

**Owning Palette:** [LVGPU SDK](../lvgpuvi/gpu_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the member data to a custom data class.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

[IMAGE alt='image' src='write_custom_data.gif']

|  | GPU Custom Data in specifies a custom data class. |
| --- | --- |
|  | Custom Data Reference specifies the data value reference containing the custom data properties. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | GPU Custom Data out returns a custom data class. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_write_data.html language=enus -->
## TOPIC 00057: Write Data VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_write_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_write_data.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Write Data VI

**Owning Palette:** [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html)

**Requires:** GPU Analysis Toolkit

Assigns the member data to a device data class. Wire data to the **CUDA U8 Device Ptr in** input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The connector pane displays the default data types for this polymorphic function.

[IMAGE alt='image' src='write_data.gif']

|  | CUDA U8 Device Ptr in specifies a device pointer class. This input also accepts a CUDA context class, a CUFFT handle class, or a CUBLAS handle class. This input can contain the following data types: 8-bit unsigned integers 16-bit unsigned integers 32-bit unsigned integers 8-bit signed integers 16-bit signed integers 32-bit signed integers Single-precision, floating-point numbers Double-precision, floating-point numbers Complex single-precision, floating-point numbers Complex double-precision, floating-point |
| --- | --- |
|  | CUDA U8 Device Ptr Data specifies the class data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | CUDA U8 Device Ptr out returns a device pointer class, CUDA context class, CUFFT handle class, or a CUBLAS handle class. This output returns the same data type that you wire to CUDA U8 Device Ptr in. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xgemm.html language=enus -->
## TOPIC 00058: xGEMM (General Matrix-Matrix Product) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xgemm.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xgemm.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xGEMM (General Matrix-Matrix Product) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the rectangular, or general, matrix expression alpha*op(*A*)*op(*B*) + b*C* for matrices *A*, *B* (if applicable), and *C*, for scalars alpha and beta, and for matrix operation op(*X*). When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xGEMM (General Matrix-Matrix Product) (aAA + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='sgemm_(aaa+bc).gif']

|  | op(B) specifies the operation the VI performs on matrix B, where matrix op(B) can equal B, B' or conj(B'). 0CUBLAS_OP_N (default)—Specifies B.1CUBLAS_OP_T—Specifies B'.2CUBLAS_OP_C—Specifies conj(B'). |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies B. |
| 1 | CUBLAS_OP_T—Specifies B'. |
| 2 | CUBLAS_OP_C—Specifies conj(B'). |
|  | op(A) specifies the operation the VI performs on matrix A, where matrix op(A) can equal A, A' or conj(A'). 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A'). |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A'). |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the square matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*op(A)*op(B). The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in matrix op(A) and C. |
|  | n specifies the number of columns to use in matrix op(B) and C. |
|  | k specifies the number of columns to use in matrix op(A) and the number of rows to use in matrix op(B). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAA+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and m columns, the VI returns the result of alpha*op(A)op(B) + bC. For any remaining elements, the VI returns the value of the element with the same index in C. |
|  | A out returns the square matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xGEMM (General Matrix-Matrix Product) (aAB + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='sgemm_(aab+bc).gif']

|  | op(B) specifies the operation the VI performs on matrix B, where matrix op(B) can equal B, B' or conj(B'). 0CUBLAS_OP_N (default)—Specifies B.1CUBLAS_OP_T—Specifies B'.2CUBLAS_OP_C—Specifies conj(B'). |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies B. |
| 1 | CUBLAS_OP_T—Specifies B'. |
| 2 | CUBLAS_OP_C—Specifies conj(B'). |
|  | op(A) specifies the operation the VI performs on matrix A, where matrix op(A) can equal A, A' or conj(A'). 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A'). |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A'). |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*op(A)*op(B). The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in matrix op(A) and C. |
|  | n specifies the number of columns to use in matrix op(B) and C. |
|  | k specifies the number of columns to use in matrix op(A) and the number of rows to use in matrix op(B). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the matrix you select, the VI replaces the result of alpha*op(A)op(B) + bC. For any remaining elements, the VI returns the value of the element with the same index in C. |
|  | A out returns the square matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xGEMM (General Matrix-Matrix Product) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xher2k.html language=enus -->
## TOPIC 00059: xHER2K (Hermitian Matrix Rank-2k Update) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xher2k.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xher2k.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xHER2K (Hermitian Matrix Rank-2k Update) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the Hermitian rank-2k update of the matrix expression alpha**A**conj(*B*') + conj(alpha)**B**conj(*A*') + beta**C* or alpha*conj(*A*')**B* + conj(alpha)*conj(*B*')**A* + beta**C*. When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xHER2K (Hermitian Matrix Rank-2k Update) (aAconj(A') + conj(a)Aconj(A') + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cher2k_(aa_a'_+__aa_a'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*conj(A') and conj(alpha)*A*conj(A'). The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A. |
|  | k specifies the number of columns to use in matrix A. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAconj(A')+conj(a)Aconj(A')+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAconj(A')+conj(a)Aconj(A')+bC returns the result of the calculation. For any remaining elements, aAconj(A')+conj(a)Aconj(A')+bC returns the value of the element with the same index in C. |
|  | A out returns the matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHER2K (Hermitian Matrix Rank-2k Update) (aconj(A')A + conj(a)conj(A')A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cher2k_(a_a'a_+__a_a'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*conj(A')*A and conj(alpha)*conj(A')*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix conj(A'). |
|  | k specifies the number of columns to use in matrix conj(A'). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aconj(A')A+conj(a)conj(A')A+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aconj(A')A+conj(a)conj(A')A+bC returns the result of the calculation. For any remaining elements, aconj(A')A+conj(a)conj(A')A+bC returns the value of the element with the same index in C. |
|  | A out returns the matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHER2K (Hermitian Matrix Rank-2k Update) (aAconj(B') + conj(a)Bconj(A') + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cher2k_(a_a'b_+__a_b'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A*conj(B)' and conj(alpha)*B*conj(A'). |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A and conj(B'). |
|  | k specifies the number of columns to use in matrix A and conj(B'). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAconj(B')+conj(a)Bconj(A')+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAconj(B')+conj(a)Bconj(A')+bC returns the result of the calculation. For any remaining elements, aAconj(B')+conj(a)Bconj(A')+bC returns the value of the element with the same index in C. |
|  | A out returns the matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHER2K (Hermitian Matrix Rank-2k Update) (aconj(A')B + conj(a)conj(B')A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cher2k_(aa_b'_+__ab_a'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*conj(A')*B and conj(alpha)*conj(B')*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix conj(A') and B. |
|  | k specifies the number of columns to use in matrix A. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aconj(A')B+conj(a)conj(B')A+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aconj(A')B+conj(a)conj(B')A+bC returns the result of the calculation. For any remaining elements, aconj(A')B+conj(a)conj(B')A+bC returns the value of the element with the same index in C. |
|  | A out returns the matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHER2K (Hermitian Matrix Rank-2k Update) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xherk.html language=enus -->
## TOPIC 00060: xHERK (Hermitian Matrix Rank-k Update) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xherk.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xherk.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xHERK (Hermitian Matrix Rank-k Update) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates a symmetric rank-k update of a symmetric matrix. When you wire data to **A in** and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xHERK (Hermitian Matrix Rank-k Update) (aAconj(A) + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cherk_(aa_a'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*conj(A') and alpha*conj(A')*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix op(A) and C. |
|  | k specifies the number of columns to use in matrix op(A). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda and ldc for A and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAconj(A')+bC returns a complex matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAconj(A')+bC returns the result of the calculation. Diagonal elements with non-zero imaginary component are set to zero. For any other elements, aAconj(A')+bC returns the value of the element in C with the same index. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHERK (Hermitian Matrix Rank-k Update) (aconj(A')A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="cherk_(a_a'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*conj(A')*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix op(A') and C. |
|  | k specifies the number of columns to use in matrix op(A'). |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda and ldc for A and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aconj(A')A+bC returns a complex matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aconj(A')A+bC returns the result of the calculation. Diagonal elements with non-zero imaginary component are set to zero. For any other elements, aconj(A')A+bC returns the value of the element in C with the same index. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHERK (Hermitian Matrix Rank-k Update) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xsymm.html language=enus -->
## TOPIC 00061: xSYMM (Symmetric Matrix-Matrix Product) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xsymm.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xsymm.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xSYMM (Symmetric Matrix-Matrix Product) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the symmetric matrix expression alpha**A***B* + beta**C* for symmetric matrix *A*, for rectangular matrices *B* (if applicable) and *C*, and for scalars alpha and beta. When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xSYMM (Symmetric Matrix-Matrix Product) (aAA + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='ssymm_(aaa_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the symmetric matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in and C. |
|  | n specifies the number of columns to use in A in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAA+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and m columns of the triangular component you select, aAA+bC returns the result of the calculation. For any remaining elements, aAA+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYMM (Symmetric Matrix-Matrix Product) (aAB + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='ssymm_(aab_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the symmetric matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in, B in, and C. |
|  | n specifies the number of columns to use in B in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component you select, aAB+bC returns the result of the calculation. For any remaining elements, aAB+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYMM (Symmetric Matrix-Matrix Product) (aBA + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='ssymm_(aba_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the symmetric matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in, B in, and C. |
|  | n specifies the number of columns to use in B in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aBA+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component you select, aBA+bC returns the result of the calculation. For any remaining elements, aBA+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYMM (Symmetric Matrix-Matrix Product) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xsyr2k.html language=enus -->
## TOPIC 00062: xSYR2K (Symmetric Matrix Rank-2k Update) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xsyr2k.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xsyr2k.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xSYR2K (Symmetric Matrix Rank-2k Update) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the rank-2k update of a symmetric matrix. When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xSYR2K (Symmetric Matrix Rank-2k Update) (aAA' + conj(a)AA' + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyr2k_(aaa'_+__aaa'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the symmetric matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A*A' and conj(alpha)*A*A'. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A. |
|  | k specifies the number of columns to use in matrix A'. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAA' + conj(a)AA'+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAA' + conj(a)AA'+bC returns the result of the calculation. For any remaining elements, aAA' + conj(a)AA'+bC returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYR2K (Symmetric Matrix Rank-2k Update) (aA'A + conj(a)A'A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyr2k_(aa'a_+__aa'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the symmetric matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A'*A and conj(alpha)*A'*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A'. |
|  | k specifies the number of columns to use in matrix A. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aA'A + conj(a)A'A+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aA'A + conj(a)A'A+bC returns the result of the calculation. For any remaining elements, aA'A + conj(a)A'A+bC returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYR2K (Symmetric Matrix Rank-2k Update) (aAB' + conj(a)BA' + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyr2k_(aab'_+__aba'_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the symmetric matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A*B' and conj(alpha)*B*A'. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix B. |
|  | k specifies the number of columns to use in matrix A. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB' + conj(a)BA'+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aAB' + conj(a)BA'+bC returns the result of the calculation. For any remaining elements, aAB' + conj(a)BA'+bC returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYR2K (Symmetric Matrix Rank-2k Update) (aA'B + conj(a)B'A + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src="ssyr2k_(aa'b_+__ab'a_+_bc).gif"]

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the symmetric matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand for the product alpha*A'*B and conj(alpha)*B'*A. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | n specifies the number of rows to use in matrix A. |
|  | k specifies the number of columns to use in matrix B. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aA'B + conj(a)B'A+bC returns a matrix with the same dimensions as C. For the elements of the first n rows and n columns of the triangular component defined by fill mode, aA'B + conj(a)B'A+bC returns the result of the calculation. For any remaining elements, aA'B + conj(a)B'A+bC returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xSYR2K (Symmetric Matrix Rank-2k Update) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xtrmm.html language=enus -->
## TOPIC 00063: xTRMM (Triangle Matrix-Matrix Product) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xtrmm.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xtrmm.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xTRMM (Triangle Matrix-Matrix Product) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the triangular matrix expression of the form alpha*op(*A*)**B* or alpha**B**op(*A*) for triangular matrix *A*, for rectangular matrices *B* and *C* (if applicable), for scalars alpha and beta, and for matrix operation op(*X*). When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

|  | Note The expressions that incorporate use of a matrix C to store the results offer better performance than those that operate on matrix B inplace. |
| --- | --- |

[Details](#details)

#### xTRMM (Triangle Matrix-Matrix Product) (aAB)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strmm_(aab).gif']

|  | operation specifies the operation the VI performs on matrix A, which results in matrix op(A) that can equal A, A' or conj(A')'. 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A')'. |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A')'. |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | B specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*op(A)*B. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in matrix op(A) and B. |
|  | n specifies the number of columns to use in B. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB returns a matrix with the same dimensions as B. For the elements of the first m rows and n columns of the triangular component defined by fill mode, the VI returns the result of alpha*op(A)*B. For any remaining elements, the VI returns the value of the element with the same index in B. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRMM (Triangle Matrix-Matrix Product) (aBA)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strmm_(aba).gif']

|  | operation specifies the operation the VI performs on matrix A, which results in matrix op(A) that can equal A, A' or conj(A')'. 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A')'. |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A')'. |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | B specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*B*op(A). The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in B. |
|  | n specifies the number of columns to use in matrix op(A) and B. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aBA returns a matrix with the same dimensions as B. For the elements of the first m rows and n columns of the triangular component defined by fill mode, the VI returns the result of alpha*B*op(A). For any remaining elements, the VI returns the value of the element with the same index in B. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRMM (Triangle Matrix-Matrix Product) (C=aAB)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strmm_(c=aab).gif']

|  | operation specifies the operation the VI performs on matrix A, which results in matrix op(A) that can equal A, A' or conj(A')'. 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A')'. |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A')'. |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*op(A)*B. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in matrix op(A) and C. |
|  | n specifies the number of columns to use in B in and C. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component defined by fill mode, the VI returns the result of alpha*op(A)*B. For any remaining elements, the VI returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRMM (Triangle Matrix-Matrix Product) (C=aBA)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strmm_(c=aba).gif']

|  | operation specifies the operation the VI performs on matrix A, which results in matrix op(A) that can equal A, A' or conj(A')'. 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A')'. |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A')'. |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the matrix C stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*B*op(A). The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in B in and C. |
|  | n specifies the number of columns to use in matrix op(A) and B. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aBA returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component defined by fill mode, the VI returns the result of alpha*B*op(A). For any remaining elements, the VI returns the value of the element with the same index in C. |
|  | A out returns the triangular matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRMM (Triangle Matrix-Matrix Product) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/gpu_xtrsm.html language=enus -->
## TOPIC 00064: xTRSM (Solve Linear Eqs - Triangle, multiple) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/gpu_xtrsm.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/gpu_xtrsm.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xTRSM (Solve Linear Eqs - Triangle, multiple) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Solves the matrix equation op(*A*)*X = alpha**B* or X*op(*A*) = alpha**B*. When you wire data to **A in** and **B**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xTRSM (Solve Linear Eqs - Triangle, multiple) (a(op[A]^-1)B)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strsm_(ab=ax).gif']

|  | operation specifies the operation the VI performs on matrix A, where matrix op(A) can equal A, A', or conj(A'). 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A'). |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A'). |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | B specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*op([A] ^-1)*B. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in B. |
|  | n specifies the number of columns to use in B. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | a(op[A]^-1)B is a complex matrix of the same dimensions as B. a(op[A]^-1)B contains the solution X, such that op(A)*X = alpha*B. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRSM (Solve Linear Eqs - Triangle, multiple) (aB(op[A]^-1))

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='strsm_(ab=xa).gif']

|  | operation specifies the operation the VI performs on matrix A, where matrix op(A) can equal A, A', or conj(A'). 0CUBLAS_OP_N (default)—Specifies A.1CUBLAS_OP_T—Specifies A'.2CUBLAS_OP_C—Specifies conj(A'). |
| --- | --- |
| 0 | CUBLAS_OP_N (default)—Specifies A. |
| 1 | CUBLAS_OP_T—Specifies A'. |
| 2 | CUBLAS_OP_C—Specifies conj(A'). |
|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | B specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the triangular matrix A stored on the device. This input specifies a class that can contain the following data types: Single-precision, floating-point numeric Double-precision, floating-point numeric Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*B*(op[A]^-1). The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in B. |
|  | n specifies the number of columns to use in B. |
|  | diag specifies the value of the diagonal elements of the triangular matrix A. 0CUBLAS_DIAG_NON_UNIT (default)1CUBLAS_DIAG_UNIT |
| 0 | CUBLAS_DIAG_NON_UNIT (default) |
| 1 | CUBLAS_DIAG_UNIT |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aB(op[A]^-1) is a complex matrix of the same dimensions as B. a(op[A]^-1)B contains the solution X, such that X*op(A) = alpha*B. |
|  | A out returns the triangular matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xTRSM (Solve Linear Eqs - Triangle, multiple) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/high_perf_analysis_pal.html language=enus -->
## TOPIC 00065: High Performance Analysis VIs

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/high_perf_analysis_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/high_perf_analysis_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### High Performance Analysis VIs

**Requires:** GPU Analysis Toolkit (Windows). This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the High Performance Analysis VIs to accelerate computations of specific mathematical and signal processing functions on parallel architectures.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Subpalette | Description |
| --- | --- |
| GPU Analysis VIs | Use the GPU Analysis VIs to interface with GPU devices from LabVIEW. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvcublas_pal.html language=enus -->
## TOPIC 00066: LVCUBLAS

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvcublas_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvcublas_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVCUBLAS

**Owning Palette:** [GPU Analysis VIs](../lvgpuvi/lvgpuvi.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the LVCUBLAS VIs to perform BLAS operations on an NVIDIA GPU device based on the NVIDIA CUBLAS library.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Version | Returns the version information for the CUBLAS library. |
| Initialize Library | Prepares the device for CUBLAS operations by providing a handle to the CUBLAS library for use in LabVIEW. |
| Release Library | Frees the initialized CUBLAS library by halting any BLAS computations in process and freeing any resources allocated during initialization for BLAS computations. |
| xGEMM (General Matrix-Matrix Product) | Calculates the rectangular, or general, matrix expression alpha*op(A)*op(B) + bC for matrices A, B (if applicable), and C, for scalars alpha and beta, and for matrix operation op(X). When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xHEMM (Hermitian Matrix-Matrix Product) | Calculates the symmetric matrix expression alpha*A*B + beta*C for symmetric matrix A, for rectangular matrices B (if applicable) and C, and for scalars alpha and beta. When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xHER2K (Hermitian Matrix Rank-2k Update) | Calculates the Hermitian rank-2k update of the matrix expression alpha*A*conj(B') + conj(alpha)*B*conj(A') + beta*C or alpha*conj(A')*B + conj(alpha)*conj(B')*A + beta*C. When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xHERK (Hermitian Matrix Rank-k Update) | Calculates a symmetric rank-k update of a symmetric matrix. When you wire data to A in and C, this VI automatically selects the first available instance. |
| xSYMM (Symmetric Matrix-Matrix Product) | Calculates the symmetric matrix expression alpha*A*B + beta*C for symmetric matrix A, for rectangular matrices B (if applicable) and C, and for scalars alpha and beta. When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xSYR2K (Symmetric Matrix Rank-2k Update) | Calculates the rank-2k update of a symmetric matrix. When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xSYRK (Symmetric Matrix Rank-k Update) | Calculates a symmetric rank-k update of a symmetric matrix. When you wire data to A in and C, this VI automatically selects the first available instance. |
| xTRMM (Triangle Matrix-Matrix Product) | Calculates the triangular matrix expression of the form alpha*op(A)*B or alpha*B*op(A) for triangular matrix A, for rectangular matrices B and C (if applicable), for scalars alpha and beta, and for matrix operation op(X). When you wire data to A in, B in (if available), and C, this VI automatically selects the first available instance. |
| xTRSM (Solve Linear Eqs - Triangle, multiple) | Solves the matrix equation op(A)*X = alpha*B or X*op(A) = alpha*B. When you wire data to A in and B, this VI automatically selects the first available instance. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvcuda_dr_api.html language=enus -->
## TOPIC 00067: LVCUDA Driver API

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvcuda_dr_api.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvcuda_dr_api.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVCUDA Driver API

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the [LVCUDA Driver API](../lvgpuvi/lvcuda_dr_api.html) VIs with the [LVCUDA SDK](../lvgpuvi/lvcuda_sdk_pal.html) VIs to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Create Context | Generates a device context, or special execution environment, in which to perform operations on the device. |
| Destroy Context | Closes the device context. This VI halts all computations in the context and frees any resources allocated to the context. |
| Get CUDA Driver API Version | Returns the version information for the CUDA driver API. The active NVIDIA display driver for the host operating system determines the CUDA Driver version. |
| Get CUDA Runtime API Version | Returns the version information for the device context. |
| Get Current Context | Retrieves the current, active device context. |
| Initialize Library | Prepares a CUDA driver API to call from LabVIEW. |
| Pop Current Context | Sets the previous device context if one exists. |
| Push Current Context | Sets the current, active device context. |
| Set Current Context | Assigns the current, active device context that replaces the previous, active context. |
| Synchronize Context | Waits for all operations running in the device context to finish. If any operation fails during synchronization, this VI returns an error. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvcuda_pal.html language=enus -->
## TOPIC 00068: LVCUDA

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvcuda_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvcuda_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVCUDA

**Owning Palette:** [GPU Analysis VIs](../lvgpuvi/lvgpuvi.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the LVCUDA VIs to manage NVIDIA GPU devices and their resources based on the NVIDIA CUDA Toolkit interface.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Allocate Memory | Acquires memory, in the form of a buffer, from the device. |
| Copy Data | Transfers copies of data between arrays in memory blocks on the device. If the array you want to copy and the device memory store different amounts of data, this VI limits the transfer to the smaller of the two amounts. |
| Download Data | Transfers data from a 1D or 2D array to memory, in the form of a buffer, on the device. If the array and the memory on the device store different amounts of data, this VI limits the transfer to the smaller of the two amounts. Wire data to the src in or dst in input to determine the polymorphic instance to use. |
| Free Memory | Releases the memory, or buffer, on the device that stores data. Wire data to the CUDA U8 Device Ptr input to determine the polymorphic instance to use. |
| Get Device | Retrieves the device ID for the device context you provide. |
| Get Device Properties | Retrieves the properties for a device using the device ID you provide. Device properties can include such properties as the device name, the amount of memory, the number of threads, and the device version. |
| Get Version Information | Returns the version information for the CUDA Runtime API, the CUDA Driver API, and the CUDA Toolkit that built the GPU Analysis Toolkit. |
| Initialize Device | Creates the special execution environment, or context, necessary for LabVIEW to communicate with the GPU. |
| Initialize Memory | Sets each byte of each element in memory on the device. This VI sets each byte up to the number of elements provided. |
| Release Device | Frees the device context and any resources allocated since initialization, including resources for communication with the device and any active processes on the device that began after initialization. This VI halts all computations in the context. |
| Synchronize Device | Waits for all operations running on the device to finish. If any operation fails during synchronization, this VI returns an error. This VI accepts a CUDA device pointer, CUDA context, CUFFT handle, CUBLAS handle. |
| Upload Data | Transfers data from memory on the device, in the form of a buffer, to a 1D or 2D LabVIEW array. If the array and the device memory store different amounts of data, this VI limits the transfer to the smaller of the two amounts. Wire data to the dst in or src in input to determine the polymorphic instance to use. |

| Subpalette | Description |
| --- | --- |
| LVCUDA Driver API | Use the LVCUDA Driver API VIs with the LVCUDA SDK VIs to build wrappers for custom GPU VIs. For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com. |
| LVCUDA SDK | Use the LVCUDA SDK to build wrappers for custom GPU VIs. For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvcuda_sdk_pal.html language=enus -->
## TOPIC 00069: LVCUDA SDK

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvcuda_sdk_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvcuda_sdk_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVCUDA SDK

**Owning Palette:** [LVCUDA](../lvgpuvi/lvcuda_pal.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the LVCUDA SDK to build wrappers for custom GPU VIs.

For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Create Data | Generates a class that stores and manages device property data, including a device memory resource and a device context. This VI also can generate a class to manage other data associated with the device, such as the execution of functions from the CUFFT library and the CUBLAS library on the device. |
| Destroy Data | Closes the class that stores and manages device data, as well as the underlying device data. When the device data controls execution or resources, this VI may halt certain functions or free resources. Wire data to the CUDA U8 Device Ptr input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |
| Get Data Properties | Retrieves the raw device data and properties in the device data class. Wire data to the CUDA U8 Device Ptr in input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |
| Prepare Data For Lock | Begins the process of locking device data. |
| Prepare Data For Unlock | Begins the process of unlocking device data. Use this VI as the last step in protecting the device data from modification or deletion while in use. Wire data to the CUDA U8 Device Ptr in input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |
| Read Data | Retrieves the member data from a device data class. Wire data to the CUDA U8 Device Ptr in input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |
| Set Data Properties | Assigns the device data and properties in the device data class. Wire data to the CUDA U8 Device Ptr in input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |
| Write Data | Assigns the member data to a device data class. Wire data to the CUDA U8 Device Ptr in input to determine the polymorphic instance to use. You can wire a CUDA device pointer, CUDA context, CUFFT handle, or CUBLAS handle to this VI. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvcufft_pal.html language=enus -->
## TOPIC 00070: LVCUFFT

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvcufft_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvcufft_pal.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LVCUFFT

**Owning Palette:** [GPU Analysis VIs](../lvgpuvi/lvgpuvi.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the LVCUFFT VIs to perform FFT transforms on an NVIDIA GPU device based on the NVIDIA CUFFT library.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Palette Object | Description |
| --- | --- |
| FFT | Computes the fast Fourier transform of signals and returns the spectrums. Wire data to the signals in input to determine the polymorphic instance or you can manually select which instance to use. |
| Get Version | Returns the version information for the CUFFT library. |
| Initialize Library | Prepares the device for FFT operations by selecting the type of FFT you want to compute. The initialization process reserves resources on the device to improve performance. |
| Inverse FFT | Computes the inverse fast Fourier transform of spectrums and returns the signals. Wire data to the spectrums in input to determine the polymorphic instance or you can manually select which instance to use. |
| Release Library | Frees the initialized CUFFT library by halting any FFT computations in process and freeing any resources allocated since initialization for FFT computations. |

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/lvgpuvi.html language=enus -->
## TOPIC 00071: GPU Analysis VIs

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/lvgpuvi.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/lvgpuvi.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### GPU Analysis VIs

**Owning Palette:** [High Performance Analysis VIs](../lvgpuvi/high_perf_analysis_pal.html)

**Requires:** GPU Analysis Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the GPU Analysis VIs to interface with GPU devices from LabVIEW.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) and [GPU Analysis error codes](../lvgpu/gpu_error_codes.html).

| Subpalette | Description |
| --- | --- |
| LVCUBLAS | Use the LVCUBLAS VIs to perform BLAS operations on an NVIDIA GPU device based on the NVIDIA CUBLAS library. |
| LVCUDA | Use the LVCUDA VIs to manage NVIDIA GPU devices and their resources based on the NVIDIA CUDA Toolkit interface. |
| LVCUFFT | Use the LVCUFFT VIs to perform FFT transforms on an NVIDIA GPU device based on the NVIDIA CUFFT library. |
| LVGPU SDK | Use the LVGPU SDK VIs to call custom GPU VIs from a LabVIEW application. For more information about how to use the LVCUDA SDK and LVGPU SDK VIs, refer to the KnowledgeBase article Customizing GPU Computing Using the GPU Analysis Toolkit at ni.com. |

© 2012 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-gpu-analysis-toolkit-api-ref path=lvgpuvi/xhemm.html language=enus -->
## TOPIC 00072: xHEMM (Hermitian Matrix-Matrix Product) VI

- bundle_id: `labview-gpu-analysis-toolkit-api-ref`
- source_path: `lvgpuvi/xhemm.html`
- source_url: https://docs-be.ni.com/bundle/labview-gpu-analysis-toolkit-api-ref/raw/resource/enus/lvgpuvi/xhemm.html
- document_id: `labview-gpu-analysis-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### xHEMM (Hermitian Matrix-Matrix Product) VI

**Owning Palette:** [LVCUBLAS](../lvgpuvi/lvcublas_pal.html)

**Requires:** GPU Analysis Toolkit

Calculates the symmetric matrix expression alpha**A***B* + beta**C* for symmetric matrix *A*, for rectangular matrices *B* (if applicable) and *C*, and for scalars alpha and beta. When you wire data to **A in**, **B in** (if available), and **C**, this VI automatically selects the first available instance.

To use a different instance, you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

[Details](#details)

#### xHEMM (Hermitian Matrix-Matrix Product) (aAA + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='chemm_(aaa_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in and C. |
|  | n specifies the number of columns to use in A in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, A, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAA+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and m columns of the triangular component you select, aAA+bC returns the result of the calculation. For any remaining elements, aAA+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHEMM (Hermitian Matrix-Matrix Product) (aAB + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='chemm_(aab_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in, B in, and C. |
|  | n specifies the number of columns to use in B in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aAB+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component you select, aAB+bC returns the result of the calculation. For any remaining elements, aAB+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHEMM (Hermitian Matrix-Matrix Product) (aBA + bC)

The connector pane displays the default data types for this polymorphic instance.

[IMAGE alt='image' src='chemm_(aba_+_bc).gif']

|  | fill mode specifies the triangular portion of the matrix A in the calculation. 0CUBLAS_FILL_MODE_LOWER (default)1CUBLAS_FILL_MODE_UPPER |
| --- | --- |
| 0 | CUBLAS_FILL_MODE_LOWER (default) |
| 1 | CUBLAS_FILL_MODE_UPPER |
|  | CUBLAS Handle in specifies the initialized CUBLAS library to use for the BLAS calculation. For example, you can wire the CUBLAS Handle output from the Initialize Library VI to specify the CUBLAS handle to the CUBLAS library you already initialized. This input also determines the device that executes the function. |
|  | C specifies the Hermitian matrix C stored on the device. The diagonal elements of C have a zero imaginary component. The calculation ignores the diagonal elements. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | A in specifies the matrix A stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | B in specifies the matrix B stored on the device. This input specifies a class that can contain the following data types: Complex single-precision, floating-point numeric Complex double-precision, floating-point numeric |
|  | a represents alpha and specifies the scalar operand in the product alpha*A*B. The default is 1. |
|  | b represents beta and specifies the scalar operand in the product beta*C. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | m specifies the number of rows to use in A in, B in, and C. |
|  | n specifies the number of columns to use in B in and C. |
|  | leading dimensions specifies the column dimension to index consecutive rows. Use lda, ldb, and ldc for A, B, and C, respectively. |
|  | CUBLAS Handle out returns the handle that defines the BLAS operation. |
|  | aBA+bC returns a matrix with the same dimensions as C. For the elements of the first m rows and n columns of the triangular component you select, aBA+bC returns the result of the calculation. For any remaining elements, aBA+bC returns the value of the element with the same index in C. |
|  | A out returns the symmetric matrix A stored on the device. |
|  | B out returns the matrix B stored on the device. |
|  | error out contains error information. This output provides standard error out functionality. |

#### xHEMM (Hermitian Matrix-Matrix Product) Details

For more information on how to use this VI, refer to the [Designing the Block Diagram to Compute on a GPU Device](../lvgpu/designing_bd_for_gpu.html) topic.

For more information about the CUBLAS library and BLAS operations, refer to the NVIDIA GPU Computing Documentation website at nvidia.com and download the CUBLAS Library User Guide.

Refer to the BLAS (Basic Linear Algebra Subprograms) website at netlib.org for more information on BLAS functions.
