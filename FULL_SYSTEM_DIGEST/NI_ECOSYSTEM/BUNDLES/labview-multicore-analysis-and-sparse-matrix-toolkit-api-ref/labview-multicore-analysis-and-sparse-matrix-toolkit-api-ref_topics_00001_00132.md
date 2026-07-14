# NI DOCUMENT BUNDLE: labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref start=1 end=132 -->
<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/analyzing_performance.html language=enus -->
## TOPIC 00001: Analyzing Performance (Multicore Analysis and Sparse Matrix Toolkit) (Windows)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/analyzing_performance.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/analyzing_performance.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analyzing Performance (Multicore Analysis and Sparse Matrix Toolkit) (Windows)

The LabVIEW Multicore Analysis and Sparse Matrix Toolkit provides [single-threading and multithreading support](#threadingcontrol) and [single- and double-precision data type support](#singleprecisionsupport). Support for these features can impact the performance of your application. Analyzing the performance of an application that uses the Multicore Analysis and Sparse Matrix Toolkit can help you take advantage of these features.

#### Multithreading Support

LabVIEW enables [multicore programming](/csh?topicname=lvconcepts/multitask_multithread_multip.html), or multiprocessing, which allows each processor in one computer to run a separate thread simultaneously. Because LabVIEW is a dataflow programming language and can automatically multithread programs, LabVIEW is ideal for overcoming multicore programming challenges.

In some computationally intensive applications, such as multi-channel signal processing, image processing, and high loop rate control and simulation, computing a single analysis function, such as matrix-matrix multiplication or the fast Fourier transform (FFT), can be very time-consuming and impede the performance of the entire application. The [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VIs are extensively parallelized to use multiple processors more efficiently. This can significantly improve performance of the entire application on multicore systems.

The following figures illustrate the computation time and performance of the [A x B](../lvmasmtref/masm_linalg_axb.html) VI in the Multicore Analysis and Sparse Matrix Toolkit. Both figures compare a different number of threads on a quad-core system running a Windows operating system.

[IMAGE alt='image' src='noloc_fp_axb_computation.gif']

In the previous figure, the A x B VI leverages the number of threads available to compute the product of two matrices. When more threads are available, the A x B VI computes the product more quickly.

[IMAGE alt='image' src='noloc_fp_axb_performance.gif']

In the previous figure, multiple threads perform more efficiently when compared to a single thread. In fact, the larger the matrix size, the greater the performance improvement of multiple threads over a single thread.

#### Single-Precision Data Type Support

The Multicore Analysis and Sparse Matrix VIs support single- and double-precision floating-point numbers. The Signal Processing VIs and Mathematics VIs support double-precision floating-point numbers only. Use of single- or double-precision floating point numbers can vary the computation time and performance of applications as the following figures illustrate. These figures compute the product of two matrices using the A x B VI in the Multicore Analysis and Sparse Matrix Toolkit.

[IMAGE alt='image' src='noloc_fp_axb_computation_single.gif']

In the previous figure, using the single-precision floating-point instance of the A x B VI computes the product of two matrices faster than the double-precision instance.

[IMAGE alt='image' src='noloc_fp_axb_performance_single.gif']

In the previous figure, the performance improvement of the single-precision floating-point instance of the A x B VI over the double-precision instance is about 2. In general, using single-precision floating-point numbers can achieve better performance and take up less memory than double-precision floating-point numbers.

|  | Note Compared with double-precision data types, loss of precision might occur when using single-precision data types. Therefore, use single-precision data types when performance improvement and memory savings are important and you will not overflow the range of the numbers. |
| --- | --- |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/direct_sparse_solver.html language=enus -->
## TOPIC 00002: Direct Sparse Solver (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/direct_sparse_solver.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/direct_sparse_solver.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Direct Sparse Solver (Multicore Analysis and Sparse Matrix Toolkit)

Solving a system of sparse linear equations depends on the matrix type. The following table shows the sparse solver method to use for different matrix types.

| Matrix Type | Sparse Solver Method |
| --- | --- |
| Lower triangular matrix | Forward substitution |
| Upper triangular matrix | Backward substitution |
| General sparse matrix | Reordering, symbolic factorization, numerical factorization, and forward and backward substitution |

If *A* is a sparse triangular matrix, to solve the sparse linear equations is straightforward. When *A* is a lower triangular matrix, the system can be solved by forward substitution. When *A* is an upper triangular matrix, the system can be solved by backward substitution. You can use the [Solve Triangular Equations](../lvmasmtref/masm_solve_triangular_eq.html) VI to solve a system if *A* is a sparse triangular matrix.

If matrix *A* is a general sparse matrix, you complete the following typical tasks to solve the system of general sparse linear equations.

- Reordering
- Symbolic factorization
- Numerical factorization
- Forward and backward substitution

#### Reordering

Decomposing a sparse matrix into its lower and upper triangular matrices tends to induce new nonzero elements into the decomposed triangular matrices. Those new nonzero elements, which are not in the original matrix *A*, are called fill-in. Fill-in can impact the sparse solver performance, because the larger the number of fill-in, the more difficult it is to store and operate the decomposed triangular matrices.

The following figure shows an example of fill-in.

[IMAGE alt='image' src='noloc_reordering_fillin.gif']

Matrix *A* has 13 nonzero elements. After decomposing matrix *A* intro its lower and upper triangular matrices *L* and *U*, all elements become nonzero.

Reordering is a process that reorders the rows and columns in matrix *A*. Reordering minimizes the fill-in in the decomposed matrices. Reordering involves the graph or sparsity pattern of the matrix. The actual values of nonzero elements in *A* are not important when reordering. Graph theory and algorithms, such as minimum degree method, determine the reordering strategy. The following figure illustrates one reordering strategy where no fill-in is induced in the decomposition.

[IMAGE alt='image' src='noloc_reordering_nofillin.gif']

#### Symbolic Factorization

The purpose of symbolic factorization is to determine the sparsity pattern in the decomposed lower and upper triangular matrices. Symbolic factorization simulates the decomposition process given the pre-defined reordering strategy. Symbolic factorization also allocates the appropriate structure and workspace for numerical factorization. Similar to reordering, symbolic factorization involves only the sparsity pattern of the original matrix *A*. Therefore, you can apply symbolic factorization to a set of matrices with the same sparsity pattern.

#### Numerical Factorization

Numerical factorization performs the actual factorization on the original matrix *A* or a sparse matrix which has the same sparsity pattern as *A*. Numerical factorization follows the simulated decomposition process by using the pre-defined reordering strategy in symbolic factorization. Also, the pre-allocated structure and workspace store the nonzero elements induced in the decomposed triangular matrices.

#### Forward and Backward Substitution

You can solve the decomposed triangular equations by forward and backward substitution. You must reorder the solution of the decomposed triangular equations to solve the original linear equations. You can repeat forward and backward substitution by using different right-hand side values of *b*. Optionally, you can improve the solution by iterative refinement.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/graphs_sparse_matrices.html language=enus -->
## TOPIC 00003: Graphs and Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/graphs_sparse_matrices.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/graphs_sparse_matrices.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Graphs and Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

Graphs and graph theory, the study of graphs, are widely used in computer science, biology, material science, sociology, and so on. A graph is an abstract representation of a set of vertices connected by edges. The set of vertices is usually numbered from 0 to *n*-1, where *n* is the total number of vertices. The method of numbering the vertices is not unique. If the graph does not distinguish between the edges from vertices *i* to *j* and *j* to *i*, the graph is an undirected graph. Otherwise, the graph is a directed graph.

A matrix can represent a graph and vice versa. Therefore, you can use matrix theory and matrix operations to solve graph problems, such as graph partition. Graphs also play an important role in sparse matrix analysis. You use graph theory in solving the system of sparse linear equations, especially in determining the [reordering](direct_sparse_solver.html#reordering) strategy.

The *n*-by-*n* adjacent matrix is the most typical matrix representation of a graph on *n* vertices. The matrix element on the (*i*, *j*) position associates with the graph edge from vertices *i* to *j*. A zero matrix element usually means that there is no connection between corresponding vertices. The adjacent matrix is symmetric if the graph is an undirected one. Otherwise, the adjacent matrix can be non-symmetric. For example, the following figure shows a graph with seven vertices and 11 edges.

[IMAGE alt='image' src='noloc_adj_matrix_graph.gif']

Suppose that the edges in the graph are undirected and not weighted. The following symmetric matrix represents the corresponding adjacent matrix.

[IMAGE alt='image' src='noloc_adj_matrix.gif']

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/lvmasmt_concepts.html language=enus -->
## TOPIC 00004: Multicore Analysis and Sparse Matrix Concepts

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/lvmasmt_concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/lvmasmt_concepts.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multicore Analysis and Sparse Matrix Concepts

This book explains how to accomplish analysis tasks by using the LabVIEW Multicore Analysis and Sparse Matrix Toolkit. This book also contains information about sparse matrix concepts.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/lvmasmt_default.html language=enus -->
## TOPIC 00005: Multicore Analysis and Sparse Matrix Toolkit

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/lvmasmt_default.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/lvmasmt_default.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multicore Analysis and Sparse Matrix Toolkit

June 2013, 373600B-01

The LabVIEW Multicore Analysis and Sparse Matrix Toolkit enables you to create applications that leverage multicore technologies. You can use the Multicore Analysis and Sparse Matrix Toolkit to compute performance-sensitive mathematics and analysis algorithms. The Multicore Analysis and Sparse Matrix Toolkit also provides sparse matrix data types and VIs which enable you to solve large-scale problems that dense matrices are unable to handle.

The Multicore Analysis and Sparse Matrix Toolkit supports Windows and NI ETS real-time operating systems only.

|  | Note The Multicore Analysis and Sparse Matrix Toolkit supports the NI ETS real-time operating system running on a PXI target or NI cRIO-908x target. |
| --- | --- |

This help file contains:

- Concepts —An overview of the Multicore Analysis and Sparse Matrix Toolkit and conceptual information that you need to understand before using the Multicore Analysis and Sparse Matrix Toolkit.
- Reference —Detailed information about the Multicore Analysis and Sparse Matrix VIs.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2011-2013 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/lvmasmt_related_doc.html language=enus -->
## TOPIC 00006: Related Documentation (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/lvmasmt_related_doc.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/lvmasmt_related_doc.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Multicore Analysis and Sparse Matrix Toolkit)

The following documents contain information that might be helpful as you use the LabVIEW Multicore Analysis and Sparse Matrix Toolkit.

- LabVIEW Multicore Analysis and Sparse Matrix Toolkit Readme—Use this file to obtain introductory information about the Multicore Analysis and Sparse Matrix Toolkit, such as product overview, system requirements, installation instructions, and known issues. Open this readme by selecting Start»All Programs»National Instruments»LabVIEW»Readme and opening readme_MASMT.html or by navigating to the labview\readme directory and opening readme_MASMT.html .
- Additional LabVIEW documentation

|  | Note The following resources offer useful background information on the general concepts discussed in this documentation. These resources are provided for general informational purposes only and are not affiliated, sponsored, or endorsed by National Instruments. The content of these resources is not a representation of, may not correspond to, and does not imply current or future functionality in the Multicore Analysis and Sparse Matrix Toolkit or any other National Instruments product. |
| --- | --- |

- Boisvert, R., R. Pozo, and K. Remington. 1996. The Matrix Market Exchange Formats: Initial Design. Rep. no. NISTIR 5935. National Institute of Standards and Technology Internal Report. December.
- Davis, Timothy A. 2006. Direct Methods for Sparse Linear Systems . Philadelphia: SIAM.
- Davis, Timothy A., and Yifan Hu. 2011. The University of Florida Sparse Matrix Collection. ACM Transactions on Mathematical Software . 38(1).
- Duff, Iain S., and Jacko Koster. 1999. The Design and Use of Algorithms for Permuting Large Entries to the Diagonal of Sparse Matrices. SIAM Journal on Matrix Analysis and Applications . 20(4):889-901.
- Gould, Nicholas I. M., Jennifer A. Scott, and Yifan Hu. 2007. A numerical evaluation of sparse direct solvers for the solution of large sparse symmetric linear systems of equations. ACM Transactions on Mathematical Software . 33(2).
- Liu, Joseph W. H. 1985. Modification of the minimum-degree algorithm by multiple elimination. ACM Transactions on Mathematical Software . 11(2):141-153.
- Schenk, Olaf, and Klaus Gartner. 2004. Solving Unsymmetric Sparse Systems of Linear Equations with PARDISO. Journal of Future Generation Computer Systems . 20(3):475--487.
- Schenk, Olaf, and Klaus Gartner. 2006. On fast factorization pivoting methods for symmetric indefinite systems. Electronic Transactions on Numerical Analysis . 23:158--179.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/managing_performance.html language=enus -->
## TOPIC 00007: Managing Performance (Multicore Analysis and Sparse Matrix Toolkit) (Windows)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/managing_performance.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/managing_performance.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Managing Performance (Multicore Analysis and Sparse Matrix Toolkit) (Windows)

When designing an application that uses multiple [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VIs, National Instruments recommends that you tweak the performance to maximize multicore performance. You can tweak the performance by [using the Multicore Analysis and Sparse Matrix VIs sequentially](#masm_vis_sequential) or by [using single-threaded Multicore Analysis and Sparse Matrix VIs in parallel](#single_threaded_masm_vis_parallel). Choosing which method to use depends on various factors, such as the size of the application problem, number of processors, number of physical cores, cache size, and so on.

|  | Note National Instruments does not recommend using the Multicore Analysis and Sparse Matrix VIs within thread control structures, such as the parallel For Loop, Timed Loop, or Timed Sequence. Using thread control structures might cause thread scheduling conflicts and diminish the performance benefit of a multicore system. In general, avoid running other computationally intensive tasks at the same time as the Multicore Analysis and Sparse Matrix VIs. |
| --- | --- |

#### Using the Multicore Analysis and Sparse Matrix VIs Sequentially

Because LabVIEW automatically multithreads, running several multithreaded Multicore Analysis and Sparse Matrix VIs simultaneously can oversubscribe the physical cores. Therefore, nested multithreading can degrade the computation performance.

Sequentially using the Multicore Analysis and Sparse Matrix VIs avoids nested multithreading, because only one VI runs at a time. You can configure the VIs to run sequentially by wiring the **error in** and **error out** terminals. The following figure shows the block diagram of a VI that runs three multithreading [FFT](/csh?topicname=lvanls/fft.html) VIs sequentially.

[IMAGE alt='image' src='noloc_bd_masm_sequential.gif']

#### Using Single-Threaded Multicore Analysis and Sparse Matrix VIs in Parallel

If the application problem size is not very large, using multithreaded Multicore Analysis and Sparse Matrix VIs does not offer significant performance advantage over single-threaded Multicore Analysis and Sparse Matrix VIs. In fact, using multithreaded Multicore Analysis and Sparse Matrix VIs can oversubscribe the physical cores. In these small size application problems, you should use single-threaded Multicore Analysis and Sparse Matrix VIs and run the VIs in parallel, as the following block diagram demonstrates.

[IMAGE alt='image' src='noloc_bd_single_thread_masm_parallel.gif']

The previous block diagram runs three single-threaded FFT VIs in parallel. You use the [Set Number of Threads](../lvmasmtref/masm_set_num_threads.html) VI to set the number of threads for parallelism. The Set Number of Threads VI on the left sets single-threading for the FFT VIs. The Set Number of Threads VI on the right sets back the number of threads to the maximum number of threads available, according to the **function domain** in the [Get Number of Threads](../lvmasmtref/masm_get_num_threads.html) VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/probing_sparse_matrices.html language=enus -->
## TOPIC 00008: Probing Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/probing_sparse_matrices.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/probing_sparse_matrices.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Probing Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

You can use [probes](/csh?topicname=lvconcepts/debug_techniques.html) to get information about a sparse matrix. You probe a sparse matrix by right-clicking on a sparse matrix wire and selecting **Probe** from the shortcut menu.

When you probe a sparse matrix, the following pages are available in the [Probe Watch Window](/csh?topicname=lvdialog/probe_watchwindow.html).

- Attributes —Returns sparse matrix attributes.
  - Representation —Returns the sparse matrix data type.
  - Number of Rows —Returns the number of rows in the sparse matrix.
  - Number of Columns —Returns the number of columns in the sparse matrix.
  - Number of Nonzeros —Returns the number of nonzero elements in the sparse matrix.
  - Max Number of Nonzeros —Returns the maximum number of nonzero elements in the sparse matrix.
  - Density (%) —Returns the density of nonzero elements in the sparse matrix.
  - Order —Returns how the elements are ordered in the sparse matrix.
- Coordinate Format —Returns the coordinate format of the sparse matrix.
  - Row Indices —Returns the row index of elements in the sparse matrix.
  - Column Indices —Returns the column index of elements in the sparse matrix.
  - Elements —Returns the value of elements in the sparse matrix.
- Dense Matrix —Displays the matrix in dense form. The size of the matrix must be 500-by-500 or smaller.
- Sparse Pattern —Displays the sparsity pattern of the matrix on an XY graph .

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/solving_partial_diff_eq_using_finite_element.html language=enus -->
## TOPIC 00009: Application of Using Sparse Matrix Operations (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/solving_partial_diff_eq_using_finite_element.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/solving_partial_diff_eq_using_finite_element.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Application of Using Sparse Matrix Operations (Multicore Analysis and Sparse Matrix Toolkit)

Sparse matrices can be useful for computing large-scale applications that dense matrices cannot handle. One such application involves solving partial differential equations by using the [finite element method](/csh?topicname=lvanlsconcepts/methods_solve_pdes.html).

The finite element method is one method of solving [partial differential equations](/csh?topicname=lvanlsconcepts/solving_pdes.html) (PDEs). Compared with another numeric method, the [finite difference method](/csh?topicname=lvanlsconcepts/methods_solve_pdes.html), the finite element method can handle geometrically complicated domains straightforwardly. The finite element method also has the flexibility to deal with problems that vary rapidly. Using the finite element method to solve PDEs involves the following steps.

1. Separate the problem domain into discrete elements.
2. Formulate the PDE into an equivalent variational problem.
3. Construct a finite dimensional subspace and determine its basis on the discrete elements.
4. Use the basic functions in the variational problem and formulate it into a system of linear equations.
5. Traverse all discrete elements and assemble the coefficient matrix and right-hand side.
6. Solve the system of linear equations to get the solution of the original PDE.

The coefficient matrix is mostly sparse. Also, the size of the coefficient matrix is large in order to get an accurate approximation to the solution of PDEs. Therefore, practical finite element method applications always rely on sparse matrices and sparse matrix operations.

Complete the following steps to use the Multicore Analysis and Sparse Matrix VIs to solve the PDE by the finite element method.

1. Compute the Delaunay triangulation of the problem domain using Delaunay Triangulation VI.
2. Initialize a sparse matrix using Initialize Matrix VI. You can specify an appropriate maximum number of nonzeros based on problem size.
3. Assemble the coefficient matrix using Set Matrix Subset VI.
4. Reorder elements in the coefficient matrix according to their row and column indices using Reorder Elements VI. A sparse matrix with reordered elements can usually hit better performance in many sparse matrix operations.
5. Solve the system of sparse linear equations using PARDISO Solver VI.

Refer to the Solve PDE by FEM VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix\Solve PDE by FEM directory for an example that uses the LabVIEW Multicore Analysis and Sparse Matrix Toolkit to solve a Poisson equation by the finite element method.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/solving_sparse_linear_eq_in_lv.html language=enus -->
## TOPIC 00010: Solving Sparse Linear Equations in LabVIEW (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/solving_sparse_linear_eq_in_lv.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/solving_sparse_linear_eq_in_lv.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Solving Sparse Linear Equations in LabVIEW (Multicore Analysis and Sparse Matrix Toolkit)

The LabVIEW Multicore Analysis and Sparse Matrix Toolkit uses the parallel direct sparse solver (PARDISO) to solve sparse linear equations. PARDISO can solve symmetric and asymmetric sparse linear systems of equations on multiprocessors. Refer to the PARDISO website at www.pardiso-project.org for more information about PARDISO.

You can use the [PARDISO Solver](../lvmasmtref/masm_pardiso_solver.html) VI and set of PARDISO advanced VIs, available on the [Sparse Linear Algebra](../lvmasmtref/masm_sparse_lin_algebra_vis.html) palette, to solve sparse symmetric, asymmetric, and positive definite systems using single or multiple right-hand sides. Use the PARDISO Solver VI to solve a system of sparse linear equations just once. Use the set of PARDISO advanced VIs to solve a system of sparse linear equations more than once. Solving a system of sparse linear equations more than once involves the following steps.

1. Initialize a solver session using the PARDISO Advanced Initialization VI. The PARDISO Advanced Initialization VI also performs reordering and symbolic factorization on the sparse matrix you specify.
2. Perform numerical factorization using the PARDISO Advanced Factorization VI. You can perform numerical factorization on the sparse matrix specified in the PARDISO Advanced Initialization VI or a sparse matrix with the same sparsity pattern.
3. Specify the right-hand side and use the PARDISO Advanced Solver VI to solve the decomposed triangular equations by forward and then backward substitution. The PARDISO Advanced Solver VI also improves the solution by iterative refinement if needed.
4. Dispose the solver session using the PARDISO Advanced Cleaning Up VI.

You may need to solve a system of sparse linear equations more than once if the coefficient matrix *A* or the sparsity pattern is fixed.

If the coefficient matrix *A* is fixed, you need to solve the system of equations repeatedly with a sequence of right-hand side *b* values. Using the set of PARDISO advanced VIs, you can perform the reordering and factorization steps once and perform the substitution step by using a [For Loop](/csh?topicname=glang/for_loop.html) that processes different right-hand side values as shown in the following block diagram.

[IMAGE alt='image' src='noloc_bd_adv_pardiso_same_matrix.gif']

If the sparsity pattern of the matrix is fixed, you need to solve the system of equations repeatedly with a sequence of coefficient matrix *A* and right-hand side *b* values. Using the set of PARDISO advanced VIs, you can perform the reordering and symbolic factorization steps once. In a For Loop, you perform the numerical factorization for the sparse matrices by using the same sparsity pattern and solve the equations with different right-hand side values by substitution, as shown in the following block diagram.

[IMAGE alt='image' src='noloc_bd_adv_pardiso_same_pattern.gif']

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/solving_sparse_linear_equations.html language=enus -->
## TOPIC 00011: Solving Sparse Linear Equations (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/solving_sparse_linear_equations.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/solving_sparse_linear_equations.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Solving Sparse Linear Equations (Multicore Analysis and Sparse Matrix Toolkit)

A system of linear equations has the form *A**x* = *b*, where *A* is an *n*-by-*n* square matrix, *b* is a given *n*-vector, and *n* is the number of elements. The aim is to determine *x*, the unknown solution *n*-vector.

When matrix *A* is a sparse matrix, this system is known as the system of sparse linear equations. A sparse solver denotes a particular method to solve the sparse linear equations.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/sparse_matrices_data_types.html language=enus -->
## TOPIC 00012: Sparse Matrix Data Types (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/sparse_matrices_data_types.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/sparse_matrices_data_types.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Sparse Matrix Data Types (Multicore Analysis and Sparse Matrix Toolkit)

The LabVIEW Multicore Analysis and Sparse Matrix Toolkit provides sparse matrix data types that support four representations:

- Double
- Single
- Complex double
- Complex single

You can create sparse matrices of different data types by using the Sparse Matrix Types controls.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/sparse_matrix_storage.html language=enus -->
## TOPIC 00013: Sparse Matrix Storage Formats (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/sparse_matrix_storage.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/sparse_matrix_storage.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Sparse Matrix Storage Formats (Multicore Analysis and Sparse Matrix Toolkit)

Sparse matrix storage formats are a specialized data structure that stores only nonzero elements in a sparse matrix. LabVIEW supports the following sparse matrix storage formats.

- Coordinate format
- Compressed sparse row format
- Compressed sparse column format

#### Coordinate Format

The coordinate format (COO) is the most flexible and simplest of the sparse matrix formats. An element in a sparse matrix is represented by a triplet (row, column, element), which specifies both the coordinate and value of the element.

For example, given the following sparse matrix,

[IMAGE alt='image' src='noloc_coo_sparse_matrix.gif']

you can represent the coordinate format as follows:

[IMAGE alt='image' src='noloc_coo.gif']

The **Row Indices** and **Column Indices** specify the row and column indices of elements in the sparse matrix, respectively. **Elements** specifies the values of elements at the corresponding coordinate. The length of these three arrays is equal to the number of nonzeros.

The elements in the coordinate format do not need to be in a specific order. However, a sparse matrix whose elements are sorted according to their row and column indices can potentially perform better during computation. You can use the [Reorder Elements](../lvmasmtref/masm_reorder_elements.html) VI to reorder the elements in a sparse matrix according to their row and column indices.

#### Compressed Sparse Row Format

The compressed sparse row format (CSR) is a variation of the coordinate format whereby the row indices are compressed. Compressing the row indices decreases memory usage. You can represent the previous sparse matrix in the compressed sparse row format as:

[IMAGE alt='image' src='noloc_csr.gif']

The length of **Compressed Row Indices** is the number of rows + 1. The elements in **Compressed Row Indices** must be in ascending order. The first element is 0 and the last element is equal to the number of nonzeros. Let *r*<sub>*i*</sub> denote the *i*-th element in **Compressed Row Indices**. Then, the *r*<sub>*i*</sub>-th to *r*<sub>*i*</sub><sub>+1</sub>-th elements in **Column Indices** specify the column index of elements in the *i*-th row in the matrix. The *r*<sub>*i*</sub>-th to *r*<sub>*i*</sub><sub>+1</sub>-th elements in **Elements** specify the value of elements at corresponding coordinate. The length of **Column Indices** and **Elements** is equal to the number of nonzeros.

#### Compressed Sparse Column Format

The compressed sparse column format (CSC) is a variation of the coordinate format whereby the column indices are compressed to decrease memory usage. You can represent the previous sparse matrix in the compressed sparse column format as:

[IMAGE alt='image' src='noloc_csc.gif']

The length of **Compressed Column Indices** is the number of columns + 1. The elements in **Compressed Column Indices** must be in ascending order. The first element is 0 and the last element is equal to the number of nonzeros. Let *c*<sub>*i*</sub> denote the *i*-th element in **Compressed Column Indices**. Then, the *c*<sub>*i*</sub>-th to *c*<sub>*i*</sub><sub>+1</sub>-th elements in **Row Indices** specify the row index of elements in the *i*-th column in the matrix. The *c*<sub>*i*</sub>-th to *c*<sub>*i*</sub><sub>+1</sub>-th elements in **Elements** specify the value of elements at corresponding coordinate. The length of **Row Indices** and **Elements** is equal to the number of nonzeros.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/understanding_sparse_matrices.html language=enus -->
## TOPIC 00014: Understanding Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/understanding_sparse_matrices.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/understanding_sparse_matrices.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Understanding Sparse Matrices (Multicore Analysis and Sparse Matrix Toolkit)

A matrix that represents a large-scale application can contain many zero elements. A matrix primarily populated by zero elements is known as a sparse matrix. Conversely, a matrix primarily populated by nonzero elements is known as a dense matrix.

To compute a dense matrix, you must store all matrix elements in memory explicitly. The computational complexity of matrix operations is proportional to the matrix size. For example, if you multiply two *n*-by-*n* matrices on a computer, where *n* is the number of rows and columns, the memory usage is *O*(*n*<sup>2</sup>) and the computational complexity is *O*(*n*<sup>3</sup>).

Therefore, working with dense matrices can be a memory-consuming and time-consuming task on a typical computer because of the potentially large size of the matrices. On the other hand, sparse matrices can use up less memory by taking advantage of the zero elements in a sparse matrix. You use a specialized [data structure](sparse_matrix_storage.html) to store the nonzero elements in the sparse matrix. Sparse matrix algorithms also contribute to faster computation.

Sparse matrices have the following attributes:

- Nonzeros —The nonzero elements in a sparse matrix. In general, the elements in a sparse matrix are nonzero elements. However, the sparse matrix in LabVIEW may store zero elements. Storing zero elements can occur in one of the following ways:
  - You explicitly set elements in a sparse matrix to zero. This is useful when you want to create a symmetrically structured sparse matrix.
  - Zero elements appear when numerical cancellation occurs in matrix operations, such as addition or subtraction. The existence of zero elements in a sparse matrix does not affect the results of matrix operations.
- Number of nonzeros —The number of nonzero elements in a sparse matrix. In LabVIEW, the number of nonzeros includes the number of zero elements if LabVIEW stores the zero elements in the sparse matrix.
- Maximum number of nonzeros —The maximum number of nonzeros elements that a sparse matrix can store. Because LabVIEW manages an internal workspace to store elements in a sparse matrix, the maximum number of nonzeros specifies the maximum number of elements that the workspace can accommodate. The maximum number of nonzeros always is no less than the number of nonzeros, such that the workspace has additional space available for inserting more elements into the sparse matrix. LabVIEW automatically enlarges the internal workspace if the number of nonzeros exceeds the maximum number of nonzeros. 
 You can use the Set Max Number of Nonzeros VI to set the maximum number of nonzeros in a sparse matrix. If the sparse matrix allows a large number of elements, specify a large value for the maximum number of nonzeros to get better performance when inserting elements.
- Density —A measure of nonzero elements in a sparse matrix. Density is equal to the ratio of the number of nonzeros to the number of rows multiplied by the number of columns.
- Pattern —The distribution of nonzero elements in a sparse matrix. Pattern, or sparsity pattern, considers the coordinates, the row and column indices, of nonzero elements more than the actual values. Two sparse matrices can have the same sparsity pattern but not the same element values.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmt/using_lvmasmt.html language=enus -->
## TOPIC 00015: Using the Multicore Analysis and Sparse Matrix Toolkit (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmt/using_lvmasmt.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmt/using_lvmasmt.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Using the Multicore Analysis and Sparse Matrix Toolkit (Multicore Analysis and Sparse Matrix Toolkit)

The LabVIEW Multicore Analysis and Sparse Matrix Toolkit provides a collection of VIs that perform high throughput signal processing and matrix computation in computationally intensive applications by leveraging multicore systems.

#### Differences Between the Multicore Analysis and Sparse Matrix VIs and the Signal Processing and Mathematics VIs

The Multicore Analysis and Sparse Matrix VIs are different from the analysis VIs and functions on the [Signal Processing](/csh?topicname=lvanls/signal_processing_vis.html) palette and [Mathematics](/csh?topicname=gmath/mathematics.html) palette in the following ways:

- (Windows) Threading control —The Multicore Analysis and Sparse Matrix VIs support single-threading and multithreading. The Signal Processing VIs and Mathematics VIs support single-threading only.
- Single-precision data type support —The Multicore Analysis and Sparse Matrix VIs support single- and double-precision floating-point numbers. The Signal Processing VIs and Mathematics VIs support double-precision floating-point numbers only.

These differences can affect VI [performance and computation](analyzing_performance.html).

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/lvmasmt_error_codes.html language=enus -->
## TOPIC 00016: Error Codes (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/lvmasmt_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/lvmasmt_error_codes.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Multicore Analysis and Sparse Matrix Toolkit)

The [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −359599 | Error occurred during thread management. Contact National Instruments for technical support. |
| −359548 | Error occurred processing out-of-core (OOC) data files. |
| −359547 | Error occurred during numerical factorization or iterative refinement. |
| −359546 | Error occurred during analysis and symbolic factorization. |
| −359545 | The solver session is invalid or corrupt. You must initialize a solver session before using it. |
| −359544 | The matrices must have the same size and sparsity pattern. |
| −359543 | The specified Matrix Market file format is not correct. |
| −359542 | The specified storage format is not correct. |
| −359541 | The sparse matrix object is invalid. You must initialize or create a sparse matrix object before using it. |
| −359521 | The real matrix computation failed. |
| −359503 | Unable to free the internal memory state of FFT. |
| −359502 | Unable to initialize the internal memory state of FFT. |
| −359501 | Unable to compute the FFT. |
| 359501 | The real matrix computation failed. LabVIEW executes the complex matrix computation instead. The result might be a complex matrix. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_abs_val.html language=enus -->
## TOPIC 00017: Absolute Value VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_abs_val.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_abs_val.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Absolute Value VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the absolute values of elements in a sparse matrix.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Absolute of Sparse Matrix (DBL)

[IMAGE alt='image' src='absolute_of_sparse_matrix__dbl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | abs(A) returns a real sparse matrix whose elements are the absolute values of elements in A. |

#### Absolute of Sparse Matrix (SGL)

[IMAGE alt='image' src='absolute_of_sparse_matrix__sgl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | abs(A) returns a real sparse matrix whose elements are the absolute values of elements in A. |

#### Absolute of Sparse Matrix (CDB)

[IMAGE alt='image' src='absolute_of_sparse_matrix__cdb.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | abs(A) returns a real sparse matrix whose elements are the absolute values of elements in A. |

#### Absolute of Sparse Matrix (CSG)

[IMAGE alt='image' src='absolute_of_sparse_matrix__csg.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | abs(A) returns a real sparse matrix whose elements are the absolute values of elements in A. |

#### Absolute Value Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: Absolute Value (CDB) Absolute Value (CSG) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_add.html language=enus -->
## TOPIC 00018: Add VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_add.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_add.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Add VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the element-wise sum of two sparse matrices.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Add Sparse to Sparse (DBL)

[IMAGE alt='image' src='add_sparse_to_sparse__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A+B returns the element-wise sum of A and B. |

#### Add Sparse to Sparse (SGL)

[IMAGE alt='image' src='add_sparse_to_sparse__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A+B returns the element-wise sum of A and B. |

#### Add Sparse to Sparse (CDB)

[IMAGE alt='image' src='add_sparse_to_sparse__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A+B returns the element-wise sum of A and B. |

#### Add Sparse to Sparse (CSG)

[IMAGE alt='image' src='add_sparse_to_sparse__csg.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A+B returns the element-wise sum of A and B. |

#### Add Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_auto_correlation.html language=enus -->
## TOPIC 00019: Auto Correlation VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_auto_correlation.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_auto_correlation.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Auto Correlation VI

**Owning Palette:** [Signal Operation VIs](../lvmasmtref/masm_signal_operation_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the auto correlation of the input sequence **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D Auto Correlation (DBL)

[IMAGE alt='image' src='1d_auto_correlation__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the auto correlation of X. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Auto Correlation (SGL)

[IMAGE alt='image' src='1d_auto_correlation__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the auto correlation of X. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Auto Correlation (CDB)

[IMAGE alt='image' src='1d_auto_correlation__cdb.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the auto correlation of X. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Auto Correlation (CSG)

[IMAGE alt='image' src='1d_auto_correlation__csg.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the auto correlation of X. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Auto Correlation (DBL)

[IMAGE alt='image' src='2d_auto_correlation__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Auto Correlation (SGL)

[IMAGE alt='image' src='2d_auto_correlation__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Auto Correlation (CDB)

[IMAGE alt='image' src='2d_auto_correlation__cdb.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Auto Correlation (CSG)

[IMAGE alt='image' src='2d_auto_correlation__csg.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxx returns the auto correlation of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Auto Correlation Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/autocorrelation.html) section in the [AutoCorrelation](/csh?topicname=lvanls/autocorrelation.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_auto_power_spectrum.html language=enus -->
## TOPIC 00020: Auto Power Spectrum VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_auto_power_spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_auto_power_spectrum.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Auto Power Spectrum VI

**Owning Palette:** [Spectral Analysis VIs](../lvmasmtref/masm_spectral_anls_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the auto power spectrum of a time-domain signal **X**. For a real input signal, the power spectrum can be either single-sided or double-sided. For a complex input signal, the power spectrum is double-sided.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Auto Power Spectrum (DBL)

[IMAGE alt='image' src='auto_power_spectrum__dbl.gif']

|  | power spectrum type specifies whether the output Power Spectrum is single-sided or double-sided. 0Single-sided (default)1Double-sided |
| --- | --- |
| 0 | Single-sided (default) |
| 1 | Double-sided |
|  | X specifies the input time-domain signal. |
|  | dt specifies the sample period of X, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal X. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the power spectrum of X. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Auto Power Spectrum (SGL)

[IMAGE alt='image' src='auto_power_spectrum__sgl.gif']

|  | power spectrum type specifies whether the output Power Spectrum is single-sided or double-sided. 0Single-sided (default)1Double-sided |
| --- | --- |
| 0 | Single-sided (default) |
| 1 | Double-sided |
|  | X specifies the input time-domain signal. |
|  | dt specifies the sample period of X, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal X. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the power spectrum of X. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Auto Power Spectrum (CDB)

[IMAGE alt='image' src='auto_power_spectrum__cdb.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | dt specifies the sample period of X, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal X. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the power spectrum of X. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Auto Power Spectrum (CSG)

[IMAGE alt='image' src='auto_power_spectrum__csg.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | dt specifies the sample period of X, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signal X. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the power spectrum of X. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Auto Power Spectrum Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

This VI computes the double-sided power spectrum using the following equation.

[IMAGE alt='image' src='noloc_eq_dbl_pwr_spectrum.gif']

where, *P*<sub>double</sub> is the double-sided **Power Spectrum** and *n* is the size of **X**.

To compute the single-sided power spectrum, this VI [converts the double-sided power spectrum to the single-sided form](/csh?topicname=lvanlsconcepts/lvac_convert_twosided_power_spec_to_singlesided.html).

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_axb.html language=enus -->
## TOPIC 00021: A x B VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_axb.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_axb.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### A x B VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the multiplication of two sparse matrices, a sparse matrix and a dense matrix, or a sparse matrix and a vector.

[Details](#details)  [Example](#examples)

#### Sparse x Sparse (DBL)

[IMAGE alt='image' src='sparse_x_sparse__dbl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Sparse (SGL)

[IMAGE alt='image' src='sparse_x_sparse__sgl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Sparse (CDB)

[IMAGE alt='image' src='sparse_x_sparse__cdb.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Sparse (CSG)

[IMAGE alt='image' src='sparse_x_sparse__csg.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Dense (DBL)

[IMAGE alt='image' src='sparse_x_dense__dbl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Dense (SGL)

[IMAGE alt='image' src='sparse_x_dense__sgl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Dense (CDB)

[IMAGE alt='image' src='sparse_x_dense__cdb.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Dense (CSG)

[IMAGE alt='image' src='sparse_x_dense__csg.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense x Sparse (DBL)

[IMAGE alt='image' src='dense_x_sparse__dbl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense x Sparse (SGL)

[IMAGE alt='image' src='dense_x_sparse__sgl.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense x Sparse (CDB)

[IMAGE alt='image' src='dense_x_sparse__cdb.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense x Sparse (CSG)

[IMAGE alt='image' src='dense_x_sparse__csg.gif']

|  | A specifies the first matrix. The number of columns in A must match the number of rows in B. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the matrix multiplication result of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Vector (DBL)

[IMAGE alt='image' src='sparse_x_vector__dbl.gif']

|  | A specifies a matrix. The number of columns in A must match the number of elements in Vector. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the matrix multiplication result of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Vector (SGL)

[IMAGE alt='image' src='sparse_x_vector__sgl.gif']

|  | A specifies a matrix. The number of columns in A must match the number of elements in Vector. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the matrix multiplication result of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Vector (CDB)

[IMAGE alt='image' src='sparse_x_vector__cdb.gif']

|  | A specifies a matrix. The number of columns in A must match the number of elements in Vector. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the matrix multiplication result of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse x Vector (CSG)

[IMAGE alt='image' src='sparse_x_vector__csg.gif']

|  | A specifies a matrix. The number of columns in A must match the number of elements in Vector. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the matrix multiplication result of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x Sparse (DBL)

[IMAGE alt='image' src='vector_x_sparse__dbl.gif']

|  | Vector specifies a vector. The number of elements in Vector must match the number of rows in A. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the matrix multiplication result of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x Sparse (SGL)

[IMAGE alt='image' src='vector_x_sparse__sgl.gif']

|  | Vector specifies a vector. The number of elements in Vector must match the number of rows in A. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the matrix multiplication result of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x Sparse (CDB)

[IMAGE alt='image' src='vector_x_sparse__cdb.gif']

|  | Vector specifies a vector. The number of elements in Vector must match the number of rows in A. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the matrix multiplication result of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x Sparse (CSG)

[IMAGE alt='image' src='vector_x_sparse__csg.gif']

|  | Vector specifies a vector. The number of elements in Vector must match the number of rows in A. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the matrix multiplication result of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x B Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: Sparse x Sparse (DBL) Sparse x Sparse (SGL) Sparse x Sparse (CDB) Sparse x Sparse (CSG) |

#### Example

Refer to the Compare Dense and Sparse A x B VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the A x B VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_blas_vis.html language=enus -->
## TOPIC 00022: Basic Linear Algebra Subroutines VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_blas_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_blas_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Basic Linear Algebra Subroutines VIs

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Basic Linear Algebra Subroutines VIs to perform basic scalar-vector, vector-vector, matrix-vector, and matrix-matrix operations.

Refer to BLAS (Basic Linear Algebra Subprograms) for more information on the BLAS functions.

| Palette Object | Description |
| --- | --- |
| gemm - General Matrix-Matrix Product | Calculates the product of two general matrices. |
| gemv - General Matrix-Vector Product | Calculates the product of a general matrix and a vector. |
| hemm - Hermitian Matrix-Matrix Product | Calculates the product of a Hermitian matrix and another matrix. |
| hemv - Hermitian Matrix-Vector Product | Calculates the product of a Hermitian matrix and a vector. |
| symm - Symmetric Matrix-Matrix Product | Calculates the product of a symmetric matrix and another matrix. |
| symv - Symmetric Matrix-Vector Product | Calculates the product of a symmetric matrix and a vector. |
| trmm - Triangular Matrix-Matrix Product | Calculates the product of a triangular matrix and another matrix. |
| trmv - Triangular Matrix-Vector Product | Calculates the product of a triangular matrix and a vector. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_build_matrix.html language=enus -->
## TOPIC 00023: Build Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_build_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_build_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Build Matrix VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Builds four sparse matrices by column and then by row.

[Details](#details)

#### Build Sparse Matrix (DBL)

[IMAGE alt='image' src='build_sparse_matrix__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows in A must be equal to the number of rows in B. The number of columns in A must be equal to the number of columns in C. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows in B must be equal to the number of rows in A. The number of columns in B must be equal to the number of columns in D. |
|  | C specifies the third sparse matrix. The number of rows in C must be equal to the number of rows in D. The number of columns in C must be equal to the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | D specifies the fourth sparse matrix. The number of rows in D must be equal to the number of rows in C. The number of columns in D must be equal to the number of columns in B. |
|  | Appended Matrix returns the appended sparse matrix of A, B, C, and D. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Build Sparse Matrix (SGL)

[IMAGE alt='image' src='build_sparse_matrix__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows in A must be equal to the number of rows in B. The number of columns in A must be equal to the number of columns in C. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows in B must be equal to the number of rows in A. The number of columns in B must be equal to the number of columns in D. |
|  | C specifies the third sparse matrix. The number of rows in C must be equal to the number of rows in D. The number of columns in C must be equal to the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | D specifies the fourth sparse matrix. The number of rows in D must be equal to the number of rows in C. The number of columns in D must be equal to the number of columns in B. |
|  | Appended Matrix returns the appended sparse matrix of A, B, C, and D. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Build Sparse Matrix (CDB)

[IMAGE alt='image' src='build_sparse_matrix__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows in A must be equal to the number of rows in B. The number of columns in A must be equal to the number of columns in C. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows in B must be equal to the number of rows in A. The number of columns in B must be equal to the number of columns in D. |
|  | C specifies the third sparse matrix. The number of rows in C must be equal to the number of rows in D. The number of columns in C must be equal to the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | D specifies the fourth sparse matrix. The number of rows in D must be equal to the number of rows in C. The number of columns in D must be equal to the number of columns in B. |
|  | Appended Matrix returns the appended sparse matrix of A, B, C, and D. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Build Sparse Matrix (CSG)

[IMAGE alt='image' src='build_sparse_matrix__csg.gif']

|  | A specifies the first sparse matrix. The number of rows in A must be equal to the number of rows in B. The number of columns in A must be equal to the number of columns in C. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows in B must be equal to the number of rows in A. The number of columns in B must be equal to the number of columns in D. |
|  | C specifies the third sparse matrix. The number of rows in C must be equal to the number of rows in D. The number of columns in C must be equal to the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | D specifies the fourth sparse matrix. The number of rows in D must be equal to the number of rows in C. The number of columns in D must be equal to the number of columns in B. |
|  | Appended Matrix returns the appended sparse matrix of A, B, C, and D. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Build Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

Let *A* be an *m*-by-*n* matrix, *B* an *n*-by-*q* matrix, *C* a *p*-by-*n* matrix, and *D* a *p*-by-*q* matrix. LabVIEW returns *H*, the appended matrix of *A*, *B*, *C*, and *D* by completing the following steps.

1. Concatenate A and B by column to get matrix F .
2. Concatenate C and D by column to get matrix G .
3. Concatenate F and G by row to get matrix H .

*H* is a (*m*+*p*)-by-(*n*+*q*) matrix.

[IMAGE alt='image' src='noloc_eq_appended_matrix.gif']

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_cholesky_decomp.html language=enus -->
## TOPIC 00024: Cholesky Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_cholesky_decomp.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_cholesky_decomp.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cholesky Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the Cholesky decomposition of a symmetric or Hermitian positive definite matrix **A**.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Cholesky Decomposition (DBL)

[IMAGE alt='image' src='cholesky_decomposition__dbl.gif']

|  | A specifies a symmetric positive definite matrix. A must be square. If A is not symmetric, this VI uses only the upper triangular portion of A. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cholesky returns the decomposed upper triangular matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cholesky Decomposition (SGL)

[IMAGE alt='image' src='cholesky_decomposition__sgl.gif']

|  | A specifies a symmetric positive definite matrix. A must be square. If A is not symmetric, this VI uses only the upper triangular portion of A. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cholesky returns the decomposed upper triangular matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cholesky Decomposition (CDB)

[IMAGE alt='image' src='cholesky_decomposition__cdb.gif']

|  | A specifies a Hermitian positive definite matrix. A must be square. If A is not Hermitian, this VI uses only the upper triangular portion of A. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cholesky returns the decomposed upper triangular matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cholesky Decomposition (CSG)

[IMAGE alt='image' src='cholesky_decomposition__csg.gif']

|  | A specifies a Hermitian positive definite matrix. A must be square. If A is not Hermitian, this VI uses only the upper triangular portion of A. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cholesky returns the decomposed upper triangular matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cholesky Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: Cholesky Decomposition (DBL) Cholesky Decomposition (CSG) |

Refer to the [Details](/csh?topicname=gmath/cholesky_factorization.html) section in the [Cholesky Factorization](/csh?topicname=gmath/cholesky_factorization.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_comparison_vis.html language=enus -->
## TOPIC 00025: Comparison VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_comparison_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_comparison_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Comparison VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Comparison VIs to compare sparse matrices.

| Palette Object | Description |
| --- | --- |
| Equal | Returns TRUE if two sparse matrices are equal. Otherwise, this VI returns FALSE. |
| Equal to Zero | Returns TRUE if Sparse Matrix is a zero matrix. Otherwise, this VI returns FALSE. |
| Not Equal | Returns TRUE if two sparse matrices are not equal. Otherwise, this VI returns FALSE. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_complex_conjugate.html language=enus -->
## TOPIC 00026: Complex Conjugate VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_complex_conjugate.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_complex_conjugate.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Complex Conjugate VI

**Owning Palette:** [Complex VIs](../lvmasmtref/masm_complex_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the complex conjugate of elements in a sparse matrix.

Wire data to the **A + iB** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Complex Conjugate Sparse Matrix (DBL)

[IMAGE alt='image' src='complex_conjugate_sparse_matrix__dbl.gif']

|  | A + iB specifies a complex sparse matrix to conjugate. |
| --- | --- |
|  | A - iB returns a complex sparse matrix whose elements are the complex conjugates of the elements in A + iB. |

#### Complex Conjugate Sparse Matrix (SGL)

[IMAGE alt='image' src='complex_conjugate_sparse_matrix__sgl.gif']

|  | A + iB specifies a complex sparse matrix to conjugate. |
| --- | --- |
|  | A - iB returns a complex sparse matrix whose elements are the complex conjugates of the elements in A + iB. |

#### Complex Conjugate Sparse Matrix (CDB)

[IMAGE alt='image' src='complex_conjugate_sparse_matrix__cdb.gif']

|  | A + iB specifies a complex sparse matrix to conjugate. |
| --- | --- |
|  | A - iB returns a complex sparse matrix whose elements are the complex conjugates of the elements in A + iB. |

#### Complex Conjugate Sparse Matrix (CSG)

[IMAGE alt='image' src='complex_conjugate_sparse_matrix__csg.gif']

|  | A + iB specifies a complex sparse matrix to conjugate. |
| --- | --- |
|  | A - iB returns a complex sparse matrix whose elements are the complex conjugates of the elements in A + iB. |

#### Complex Conjugate Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: Complex Conjugate (DBL) Complex Conjugate (SGL) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_complex_to_re_im.html language=enus -->
## TOPIC 00027: Complex To Re Im VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_complex_to_re_im.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_complex_to_re_im.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Complex To Re Im VI

**Owning Palette:** [Complex VIs](../lvmasmtref/masm_complex_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Breaks the real and imaginary parts of a complex sparse matrix into two real sparse matrices.

Wire data to the **A + iB** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Complex Sparse Matrix To Re Im (DBL)

[IMAGE alt='image' src='complex_sparse_matrix_to_re_im__dbl.gif']

|  | A + iB specifies a complex sparse matrix to separate into real and imaginary parts. |
| --- | --- |
|  | A returns a real sparse matrix whose elements are the real parts of the elements in A + iB. |
|  | B returns a real sparse matrix whose elements are the imaginary parts of the elements in A + iB. |

#### Complex Sparse Matrix To Re Im (SGL)

[IMAGE alt='image' src='complex_sparse_matrix_to_re_im__sgl.gif']

|  | A + iB specifies a complex sparse matrix to separate into real and imaginary parts. |
| --- | --- |
|  | A returns a real sparse matrix whose elements are the real parts of the elements in A + iB. |
|  | B returns a real sparse matrix whose elements are the imaginary parts of the elements in A + iB. |

#### Complex Sparse Matrix To Re Im (CDB)

[IMAGE alt='image' src='complex_sparse_matrix_to_re_im__cdb.gif']

|  | A + iB specifies a complex sparse matrix to separate into real and imaginary parts. |
| --- | --- |
|  | A returns a real sparse matrix whose elements are the real parts of the elements in A + iB. |
|  | B returns a real sparse matrix whose elements are the imaginary parts of the elements in A + iB. |

#### Complex Sparse Matrix To Re Im (CSG)

[IMAGE alt='image' src='complex_sparse_matrix_to_re_im__csg.gif']

|  | A + iB specifies a complex sparse matrix to separate into real and imaginary parts. |
| --- | --- |
|  | A returns a real sparse matrix whose elements are the real parts of the elements in A + iB. |
|  | B returns a real sparse matrix whose elements are the imaginary parts of the elements in A + iB. |

#### Complex To Re Im Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_complex_vis.html language=enus -->
## TOPIC 00028: Complex VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_complex_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_complex_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Complex VIs

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Complex VIs to create a complex sparse matrix as its real and imaginary components from two real sparse matrices and to break the real and imaginary components of a complex sparse matrix into two real sparse matrices.

| Palette Object | Description |
| --- | --- |
| Complex Conjugate | Computes the complex conjugate of elements in a sparse matrix. |
| Complex To Re Im | Breaks the real and imaginary parts of a complex sparse matrix into two real sparse matrices. |
| Re Im To Complex | Creates a complex sparse matrix from two real sparse matrices containing real and imaginary parts, respectively. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_concatenate_matrix.html language=enus -->
## TOPIC 00029: Concatenate Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_concatenate_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_concatenate_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Concatenate Matrix VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Concatenates two sparse matrices by row, column, or diagonal.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Concatenate Sparse Matrix (DBL)

[IMAGE alt='image' src='concatenate_sparse_matrix__dbl.gif']

|  | A specifies the first sparse matrix. |
| --- | --- |
|  | B specifies the second sparse matrix. |
|  | direction specifies the direction to concatenate A and B. 0Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A.1Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A.2Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
| 0 | Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A. |
| 1 | Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A. |
| 2 | Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Concatenated Matrix returns the concatenated sparse matrix of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Concatenate Sparse Matrix (SGL)

[IMAGE alt='image' src='concatenate_sparse_matrix__sgl.gif']

|  | A specifies the first sparse matrix. |
| --- | --- |
|  | B specifies the second sparse matrix. |
|  | direction specifies the direction to concatenate A and B. 0Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A.1Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A.2Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
| 0 | Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A. |
| 1 | Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A. |
| 2 | Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Concatenated Matrix returns the concatenated sparse matrix of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Concatenate Sparse Matrix (CDB)

[IMAGE alt='image' src='concatenate_sparse_matrix__cdb.gif']

|  | A specifies the first sparse matrix. |
| --- | --- |
|  | B specifies the second sparse matrix. |
|  | direction specifies the direction to concatenate A and B. 0Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A.1Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A.2Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
| 0 | Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A. |
| 1 | Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A. |
| 2 | Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Concatenated Matrix returns the concatenated sparse matrix of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Concatenate Sparse Matrix (CSG)

[IMAGE alt='image' src='concatenate_sparse_matrix__csg.gif']

|  | A specifies the first sparse matrix. |
| --- | --- |
|  | B specifies the second sparse matrix. |
|  | direction specifies the direction to concatenate A and B. 0Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A.1Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A.2Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
| 0 | Row—Specifies that this VI concatenates A and B by row. LabVIEW adds B to the last row starting with the first column in A. |
| 1 | Column (default)—Specifies this that VI concatenates A and B by column. LabVIEW adds B to the last column starting with the first row in A. |
| 2 | Diagonal—Specifies that this VI concatenates A and B by diagonal. LabVIEW adds B to the last row starting with the last column in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Concatenated Matrix returns the concatenated sparse matrix of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Concatenate Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

Let *A* be an *m*-by-*n* matrix and *B* a *p*-by-*q* matrix. Let *C* be the concatenated matrix of *A* and *B*.

##### Concatenate *A* and *B* by Row

*C* is a (*m*+*p*)-by-max(*n*, *q*) matrix.

[IMAGE alt='image' src='noloc_eq_concatenate_by_row.gif']

##### Concatenate *A* and *B* by Column

*C* is a max(*m*, *p*)-by-(*n*+*q*) matrix.

[IMAGE alt='image' src='noloc_eq_concatenate_by_column.gif']

##### Concatenate *A* and *B* by Diagonal

*C* is a (*m*+*p*)-by-(*n*+*q*) matrix.

[IMAGE alt='image' src='noloc_eq_concatenate_by_diagonal.gif']

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_conversion_vis.html language=enus -->
## TOPIC 00030: Conversion VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_conversion_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_conversion_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Conversion VIs

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Conversion VIs to convert sparse matrix data types.

| Palette Object | Description |
| --- | --- |
| To Double Precision Complex | Converts elements in a sparse matrix to double-precision, complex numbers. |
| To Double Precision Float | Converts elements in a sparse matrix to double-precision, floating-point numbers. |
| To Single Precision Complex | Converts elements in a sparse matrix to single-precision, complex numbers. |
| To Single Precision Float | Converts elements in a sparse matrix to single-precision, floating-point numbers. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_convolution.html language=enus -->
## TOPIC 00031: Convolution VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_convolution.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_convolution.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Convolution VI

**Owning Palette:** [Signal Operation VIs](../lvmasmtref/masm_signal_operation_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the convolution of the input sequences **X** and **Y**.

Wire data to the **X** input and the **Y** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D Convolution (DBL)

[IMAGE alt='image' src='1d_convolution__dbl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. 0Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. 1Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. 2Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
| 0 | Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. |
| 1 | Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. |
| 2 | Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Convolution (SGL)

[IMAGE alt='image' src='1d_convolution__sgl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. 0Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. 1Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. 2Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
| 0 | Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. |
| 1 | Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. |
| 2 | Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Convolution (CDB)

[IMAGE alt='image' src='1d_convolution__cdb.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. 0Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. 1Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. 2Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
| 0 | Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. |
| 1 | Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. |
| 2 | Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Convolution (CSG)

[IMAGE alt='image' src='1d_convolution__csg.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. 0Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. 1Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. 2Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
| 0 | Full (default)—Sets the length of X * Y to one less than the sum of the lengths of X and Y. The output vector X * Y is: where h(full) is X * Y, N is the length of X, M is the length of Y. The indexed elements outside the ranges of X and Y are equal to zero, as shown in the following relationships. |
| 1 | Size X—Sets the length of X * Y to the length of X. The output vector X * Y is of the same length of X and is the central part of the output vector X * Y when the output size is Full, as shown in the following equation. |
| 2 | Compact—Sets the length of X * Y to one more than the difference between the lengths of X and Y. The length of X must be greater than or equal to the length of Y. Computing the edge elements of X * Y requires zero-padding if the output size is Full or Size X. LabVIEW removes these edge elements if the output size is Compact. The output vector X * Y is the central part of the output vector X * Y when the output size is Size X or Full, as shown in the following equation. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Convolution (DBL)

[IMAGE alt='image' src='2d_convolution__dbl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. Refer to the Details section in the Convolution VI for more details about output size in 2D instances of this VI. 0Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y.1Size X—Sets the width and height of X * Y to the width and height of X.2Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
| 0 | Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y. |
| 1 | Size X—Sets the width and height of X * Y to the width and height of X. |
| 2 | Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Convolution (SGL)

[IMAGE alt='image' src='2d_convolution__sgl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. Refer to the Details section in the Convolution VI for more details about output size in 2D instances of this VI. 0Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y.1Size X—Sets the width and height of X * Y to the width and height of X.2Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
| 0 | Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y. |
| 1 | Size X—Sets the width and height of X * Y to the width and height of X. |
| 2 | Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Convolution (CDB)

[IMAGE alt='image' src='2d_convolution__cdb.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. Refer to the Details section in the Convolution VI for more details about output size in 2D instances of this VI. 0Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y.1Size X—Sets the width and height of X * Y to the width and height of X.2Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
| 0 | Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y. |
| 1 | Size X—Sets the width and height of X * Y to the width and height of X. |
| 2 | Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Convolution (CSG)

[IMAGE alt='image' src='2d_convolution__csg.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the convolution method to use. When algorithm is Direct, this VI computes the convolution using the direct method of linear convolution. When algorithm is Frequency Domain, this VI computes the convolution using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. Refer to the Details section in the Convolution VI for more details about algorithm in this VI. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | output size specifies the size of X * Y. Refer to the Details section in the Convolution VI for more details about output size in 2D instances of this VI. 0Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y.1Size X—Sets the width and height of X * Y to the width and height of X.2Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
| 0 | Full (default)—Sets the width of X * Y to one less than the sum of the widths of X and Y and sets the height of X * Y to one less than the sum of the heights of X and Y. |
| 1 | Size X—Sets the width and height of X * Y to the width and height of X. |
| 2 | Compact—Sets the width of X * Y to one more than the difference between the widths of X and Y and sets the height of X * Y to one more than the difference of the heights of X and Y. The width and height of X must be greater than or equal to the width and height of Y, respectively. |
|  | X * Y returns the convolution of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Convolution Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/convolution.html) section in the [Convolution](/csh?topicname=lvanls/convolution.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_create_matrix_from_storage_form.html language=enus -->
## TOPIC 00032: Create Matrix from Storage Format VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_create_matrix_from_storage_form.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_create_matrix_from_storage_form.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Matrix from Storage Format VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Creates a sparse matrix from storage format.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Create Sparse Matrix from COO (DBL)

[IMAGE alt='image' src='create_sparse_matrix_from_coo__dbl.gif']

|  | Row Indices specifies the row indices of elements in the coordinate format. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the coordinate format. The number of elements in Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the coordinate format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from COO (SGL)

[IMAGE alt='image' src='create_sparse_matrix_from_coo__sgl.gif']

|  | Row Indices specifies the row indices of elements in the coordinate format. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the coordinate format. The number of elements in Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the coordinate format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from COO (CDB)

[IMAGE alt='image' src='create_sparse_matrix_from_coo__cdb.gif']

|  | Row Indices specifies the row indices of elements in the coordinate format. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the coordinate format. The number of elements in Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the coordinate format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from COO (CSG)

[IMAGE alt='image' src='create_sparse_matrix_from_coo__csg.gif']

|  | Row Indices specifies the row indices of elements in the coordinate format. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the coordinate format. The number of elements in Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the coordinate format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSR (DBL)

[IMAGE alt='image' src='create_sparse_matrix_from_csr__dbl.gif']

|  | Compressed Row Indices specifies the compressed Row indices of elements in the compressed sparse row format. The number of elements in Compressed Row Indices must be equal to the number of rows+1. The first element in Compressed Row Indices must be 0 and the last element must be equal to the number of elements in Column Indices. All elements in Compressed Row Indices must be in ascending order. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Elements. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the compressed sparse row format. The number of elements in Elements must be equal to the number of elements in Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Compressed Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse row format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSR (SGL)

[IMAGE alt='image' src='create_sparse_matrix_from_csr__sgl.gif']

|  | Compressed Row Indices specifies the compressed Row indices of elements in the compressed sparse row format. The number of elements in Compressed Row Indices must be equal to the number of rows+1. The first element in Compressed Row Indices must be 0 and the last element must be equal to the number of elements in Column Indices. All elements in Compressed Row Indices must be in ascending order. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Elements. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the compressed sparse row format. The number of elements in Elements must be equal to the number of elements in Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Compressed Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse row format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSR (CDB)

[IMAGE alt='image' src='create_sparse_matrix_from_csr__cdb.gif']

|  | Compressed Row Indices specifies the compressed Row indices of elements in the compressed sparse row format. The number of elements in Compressed Row Indices must be equal to the number of rows+1. The first element in Compressed Row Indices must be 0 and the last element must be equal to the number of elements in Column Indices. All elements in Compressed Row Indices must be in ascending order. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Elements. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the compressed sparse row format. The number of elements in Elements must be equal to the number of elements in Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Compressed Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse row format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSR (CSG)

[IMAGE alt='image' src='create_sparse_matrix_from_csr__csg.gif']

|  | Compressed Row Indices specifies the compressed Row indices of elements in the compressed sparse row format. The number of elements in Compressed Row Indices must be equal to the number of rows+1. The first element in Compressed Row Indices must be 0 and the last element must be equal to the number of elements in Column Indices. All elements in Compressed Row Indices must be in ascending order. |
| --- | --- |
|  | Column Indices specifies the column indices of elements in the coordinate format. The number of elements in Column Indices must be equal to the number of elements in Elements. All elements in Column Indices must be non-negative and smaller than number of columns. |
|  | Elements specifies the value of elements in the compressed sparse row format. The number of elements in Elements must be equal to the number of elements in Column Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Compressed Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse row format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSC (DBL)

[IMAGE alt='image' src='create_sparse_matrix_from_csc__dbl.gif']

|  | Row Indices specifies the row indices of the elements in the compressed sparse column format. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Compressed Column Indices specifies the compressed column indices of elements in the compressed sparse column format. The number of elements in Compressed Column Indices must be equal to the number of columns+1. The first element in Compressed Column Indices must be 0 and the last element must be equal to the number of elements in Row Indices. All elements in Compressed Column Indices must be in ascending order. |
|  | Elements specifies the value of the elements in the compressed sparse column format. The number of elements in Elements must be equal to the number of elements in Row Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Compressed Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse column format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSC (SGL)

[IMAGE alt='image' src='create_sparse_matrix_from_csc__sgl.gif']

|  | Row Indices specifies the row indices of the elements in the compressed sparse column format. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Compressed Column Indices specifies the compressed column indices of elements in the compressed sparse column format. The number of elements in Compressed Column Indices must be equal to the number of columns+1. The first element in Compressed Column Indices must be 0 and the last element must be equal to the number of elements in Row Indices. All elements in Compressed Column Indices must be in ascending order. |
|  | Elements specifies the value of the elements in the compressed sparse column format. The number of elements in Elements must be equal to the number of elements in Row Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Compressed Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse column format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSC (CDB)

[IMAGE alt='image' src='create_sparse_matrix_from_csc__cdb.gif']

|  | Row Indices specifies the row indices of the elements in the compressed sparse column format. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Compressed Column Indices specifies the compressed column indices of elements in the compressed sparse column format. The number of elements in Compressed Column Indices must be equal to the number of columns+1. The first element in Compressed Column Indices must be 0 and the last element must be equal to the number of elements in Row Indices. All elements in Compressed Column Indices must be in ascending order. |
|  | Elements specifies the value of the elements in the compressed sparse column format. The number of elements in Elements must be equal to the number of elements in Row Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Compressed Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse column format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Sparse Matrix from CSC (CSG)

[IMAGE alt='image' src='create_sparse_matrix_from_csc__csg.gif']

|  | Row Indices specifies the row indices of the elements in the compressed sparse column format. All elements in Row Indices must be non-negative and smaller than number of rows. |
| --- | --- |
|  | Compressed Column Indices specifies the compressed column indices of elements in the compressed sparse column format. The number of elements in Compressed Column Indices must be equal to the number of columns+1. The first element in Compressed Column Indices must be 0 and the last element must be equal to the number of elements in Row Indices. All elements in Compressed Column Indices must be in ascending order. |
|  | Elements specifies the value of the elements in the compressed sparse column format. The number of elements in Elements must be equal to the number of elements in Row Indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows specifies the number of rows in Sparse Matrix. If number of rows is negative, LabVIEW determines the number of rows from Row Indices. The default is -1. |
|  | number of columns specifies the number of columns in Sparse Matrix. If number of columns is negative, LabVIEW determines the number of columns from Compressed Column Indices. The default is -1. |
|  | Sparse Matrix returns the sparse matrix created from the compressed sparse column format. If two or more elements have identical row and column indices, LabVIEW receives the last element in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Matrix from Storage Format Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_create_random_matrix.html language=enus -->
## TOPIC 00033: Create Random Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_create_random_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_create_random_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Random Matrix VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Generates a sparse matrix randomly.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Create Random Matrix (DBL)

[IMAGE alt='image' src='create_random_matrix__dbl.gif']

|  | distribution specifies the distribution of the elements in Sparse Matrix. 0Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1].1Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
| --- | --- |
| 0 | Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1]. |
| 1 | Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
|  | matrix type specifies the type of sparse matrix to create. 0General (default)—Specifies to create a general sparse matrix.2Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix.3Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 0 | General (default)—Specifies to create a general sparse matrix. |
| 2 | Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 3 | Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be positive. |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be positive. |
|  | density specifies the density of elements in Sparse Matrix. The number of elements in Sparse Matrix equals to density*number of rows*number of columns. The density must range from 0 to 1. The default is 0.01. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | seed specifies how this VI generates the sparse matrix randomly. If seed is greater than 0, LabVIEW uses seed to generate the internal state directly. If seed is less than or equal to 0, LabVIEW uses a random number to generate the internal state. The default is -1. |
|  | Sparse Matrix returns the randomly created sparse matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Random Matrix (SGL)

[IMAGE alt='image' src='create_random_matrix__sgl.gif']

|  | distribution specifies the distribution of the elements in Sparse Matrix. 0Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1].1Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
| --- | --- |
| 0 | Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1]. |
| 1 | Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
|  | matrix type specifies the type of sparse matrix to create. 0General (default)—Specifies to create a general sparse matrix.2Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix.3Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 0 | General (default)—Specifies to create a general sparse matrix. |
| 2 | Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 3 | Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be positive. |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be positive. |
|  | density specifies the density of elements in Sparse Matrix. The number of elements in Sparse Matrix equals to density*number of rows*number of columns. The density must range from 0 to 1. The default is 0.01. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | seed specifies how this VI generates the sparse matrix randomly. If seed is greater than 0, LabVIEW uses seed to generate the internal state directly. If seed is less than or equal to 0, LabVIEW uses a random number to generate the internal state. The default is -1. |
|  | Sparse Matrix returns the randomly created sparse matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Random Matrix (CDB)

[IMAGE alt='image' src='create_random_matrix__cdb.gif']

|  | distribution specifies the distribution of the elements in Sparse Matrix. 0Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1].1Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
| --- | --- |
| 0 | Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1]. |
| 1 | Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
|  | matrix type specifies the type of sparse matrix to create. 0General (default)—Specifies to create a general sparse matrix.2Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix.3Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 0 | General (default)—Specifies to create a general sparse matrix. |
| 2 | Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 3 | Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be positive. |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be positive. |
|  | density specifies the density of elements in Sparse Matrix. The number of elements in Sparse Matrix equals to density*number of rows*number of columns. The density must range from 0 to 1. The default is 0.01. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | seed specifies how this VI generates the sparse matrix randomly. If seed is greater than 0, LabVIEW uses seed to generate the internal state directly. If seed is less than or equal to 0, LabVIEW uses a random number to generate the internal state. The default is -1. |
|  | Sparse Matrix returns the randomly created sparse matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Random Matrix (CSG)

[IMAGE alt='image' src='create_random_matrix__csg.gif']

|  | distribution specifies the distribution of the elements in Sparse Matrix. 0Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1].1Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
| --- | --- |
| 0 | Uniform (default)—Specifies that the elements in Sparse Matrix are uniformly distributed and whose values are in the range [-1, 1]. |
| 1 | Gaussian—Specifies that the elements in Sparse Matrix are standard Gaussian-distributed. |
|  | matrix type specifies the type of sparse matrix to create. 0General (default)—Specifies to create a general sparse matrix.2Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix.3Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 0 | General (default)—Specifies to create a general sparse matrix. |
| 2 | Lower Triangular—Specifies to create a lower triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
| 3 | Upper Triangular—Specifies to create an upper triangular sparse matrix. The elements on the main diagonal are always created in Sparse Matrix. |
|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be positive. |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be positive. |
|  | density specifies the density of elements in Sparse Matrix. The number of elements in Sparse Matrix equals to density*number of rows*number of columns. The density must range from 0 to 1. The default is 0.01. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | seed specifies how this VI generates the sparse matrix randomly. If seed is greater than 0, LabVIEW uses seed to generate the internal state directly. If seed is less than or equal to 0, LabVIEW uses a random number to generate the internal state. The default is -1. |
|  | Sparse Matrix returns the randomly created sparse matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Random Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_create_special_sparse_matrix.html language=enus -->
## TOPIC 00034: Create Special Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_create_special_sparse_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_create_special_sparse_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Special Matrix VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Creates a sparse matrix of a specific type.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Create Special Matrix (DBL)

[IMAGE alt='image' src='create_special_matrix_sparse_dbl.gif']

|  | matrix type specifies the type of sparse matrix to create. 0Identity (default)—Specifies to create an identity sparse matrix.1Diagonal—Specifies to create a diagonal sparse matrix. |
| --- | --- |
| 0 | Identity (default)—Specifies to create an identity sparse matrix. |
| 1 | Diagonal—Specifies to create a diagonal sparse matrix. |
|  | matrix size specifies the dimension size of Sparse Matrix. LabVIEW does not use matrix size if matrix type is Diagonal. If matrix type is Identity, matrix size must be positive. The default is 1. |
|  | Input Vector specifies the input to construct the main diagonal in Sparse Matrix. LabVIEW does not use Input Vector if matrix type is Identity. The Input Vector must not be empty if matrix type is Diagonal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the number automatically. The default is -1. |
|  | Sparse Matrix returns the sparse matrix of a specific matrix type that this VI creates. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (SGL)

[IMAGE alt='image' src='create_special_matrix_sparse_sgl.gif']

|  | matrix type specifies the type of sparse matrix to create. 0Identity (default)—Specifies to create an identity sparse matrix.1Diagonal—Specifies to create a diagonal sparse matrix. |
| --- | --- |
| 0 | Identity (default)—Specifies to create an identity sparse matrix. |
| 1 | Diagonal—Specifies to create a diagonal sparse matrix. |
|  | matrix size specifies the dimension size of Sparse Matrix. LabVIEW does not use matrix size if matrix type is Diagonal. If matrix type is Identity, matrix size must be positive. The default is 1. |
|  | Input Vector specifies the input to construct the main diagonal in Sparse Matrix. LabVIEW does not use Input Vector if matrix type is Identity. The Input Vector must not be empty if matrix type is Diagonal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the number automatically. The default is -1. |
|  | Sparse Matrix returns the sparse matrix of a specific matrix type that this VI creates. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (CDB)

[IMAGE alt='image' src='create_special_matrix_sparse_cdb.gif']

|  | matrix type specifies the type of sparse matrix to create. 0Identity (default)—Specifies to create an identity sparse matrix.1Diagonal—Specifies to create a diagonal sparse matrix. |
| --- | --- |
| 0 | Identity (default)—Specifies to create an identity sparse matrix. |
| 1 | Diagonal—Specifies to create a diagonal sparse matrix. |
|  | matrix size specifies the dimension size of Sparse Matrix. LabVIEW does not use matrix size if matrix type is Diagonal. If matrix type is Identity, matrix size must be positive. The default is 1. |
|  | Input Vector specifies the input to construct the main diagonal in Sparse Matrix. LabVIEW does not use Input Vector if matrix type is Identity. The Input Vector must not be empty if matrix type is Diagonal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the number automatically. The default is -1. |
|  | Sparse Matrix returns the sparse matrix of a specific matrix type that this VI creates. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (CSG)

[IMAGE alt='image' src='create_special_matrix_sparse_csg.gif']

|  | matrix type specifies the type of sparse matrix to create. 0Identity (default)—Specifies to create an identity sparse matrix.1Diagonal—Specifies to create a diagonal sparse matrix. |
| --- | --- |
| 0 | Identity (default)—Specifies to create an identity sparse matrix. |
| 1 | Diagonal—Specifies to create a diagonal sparse matrix. |
|  | matrix size specifies the dimension size of Sparse Matrix. LabVIEW does not use matrix size if matrix type is Diagonal. If matrix type is Identity, matrix size must be positive. The default is 1. |
|  | Input Vector specifies the input to construct the main diagonal in Sparse Matrix. LabVIEW does not use Input Vector if matrix type is Identity. The Input Vector must not be empty if matrix type is Diagonal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the number automatically. The default is -1. |
|  | Sparse Matrix returns the sparse matrix of a specific matrix type that this VI creates. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_cross_correlation.html language=enus -->
## TOPIC 00035: Cross Correlation VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_cross_correlation.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_cross_correlation.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cross Correlation VI

**Owning Palette:** [Signal Operation VIs](../lvmasmtref/masm_signal_operation_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the cross correlation of the input sequences **X** and **Y**.

Wire data to the **X** input and the **Y** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D Cross Correlation (DBL)

[IMAGE alt='image' src='1d_cross_correlation__dbl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the cross correlation of X and Y. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Cross Correlation (SGL)

[IMAGE alt='image' src='1d_cross_correlation__sgl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the cross correlation of X and Y. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Cross Correlation (CDB)

[IMAGE alt='image' src='1d_cross_correlation__cdb.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the cross correlation of X and Y. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Cross Correlation (CSG)

[IMAGE alt='image' src='1d_cross_correlation__csg.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | normalization specifies the normalization method to use to compute the cross correlation of X and Y. 0None (default)1Unbiased2Biased |
| 0 | None (default) |
| 1 | Unbiased |
| 2 | Biased |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Cross Correlation (DBL)

[IMAGE alt='image' src='2d_cross_correlation__dbl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Cross Correlation (SGL)

[IMAGE alt='image' src='2d_cross_correlation__sgl.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Cross Correlation (CDB)

[IMAGE alt='image' src='2d_cross_correlation__cdb.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Cross Correlation (CSG)

[IMAGE alt='image' src='2d_cross_correlation__csg.gif']

|  | X specifies the first input sequence. |
| --- | --- |
|  | Y specifies the second input sequence. |
|  | algorithm specifies the correlation method to use. When algorithm is Direct, this VI computes the cross correlation using the direct method of linear correlation. When algorithm is Frequency Domain, this VI computes the cross correlation using an FFT-based technique. If X and Y are small, the Direct method typically computes faster than the Frequency Domain method. If X and Y are large, the Frequency Domain method typically computes faster than the Direct method. Slight numerical differences can exist between the two methods. 0Direct1Frequency Domain (default) |
| 0 | Direct |
| 1 | Frequency Domain (default) |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Rxy returns the cross correlation of X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Correlation Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/crosscorrelation.html) section in the [CrossCorrelation](/csh?topicname=lvanls/crosscorrelation.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_cross_power.html language=enus -->
## TOPIC 00036: Cross Power VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_cross_power.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_cross_power.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cross Power VI

**Owning Palette:** [Spectral Analysis VIs](../lvmasmtref/masm_spectral_anls_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the double-sided cross power spectrum of two time-domain signals **X** and **Y**.

Wire data to the **X** and **Y** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Cross Power (DBL)

[IMAGE alt='image' src='cross_power__dbl.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sxy returns the cross power spectrum of signals X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power (SGL)

[IMAGE alt='image' src='cross_power__sgl.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sxy returns the cross power spectrum of signals X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power (CDB)

[IMAGE alt='image' src='cross_power__cdb.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sxy returns the cross power spectrum of signals X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power (CSG)

[IMAGE alt='image' src='cross_power__csg.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sxy returns the cross power spectrum of signals X and Y. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

If the input signals **X** and **Y** have different lengths, this VI first pads zeros to the shorter input signal to make the signals the same length. Let *n* represent the common length of the two signals after this VI pads zeros to the end of the shorter input signal.

This VI computes the double-sided cross power spectrum using the following equation.

[IMAGE alt='image' src='noloc_eq_dbl_cross_pwr_spectrum.gif']

where *P*<sub>double</sub> is the double-sided cross power spectrum **Sxy**.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_cross_power_spectrum.html language=enus -->
## TOPIC 00037: Cross Power Spectrum VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_cross_power_spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_cross_power_spectrum.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Cross Power Spectrum VI

**Owning Palette:** [Spectral Analysis VIs](../lvmasmtref/masm_spectral_anls_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the cross power spectrum of two time-domain signals **X** and **Y**. For real input signals, the cross power spectrum can be either single-sided or double-sided. For complex input signals, the cross power spectrum is double-sided.

Wire data to the **X** and **Y** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Cross Power Spectrum (DBL)

[IMAGE alt='image' src='cross_power_spectrum__dbl.gif']

|  | power spectrum type specifies whether the output Cross Power Spectrum is single-sided or double-sided. 0Single-sided (default)1Double-sided |
| --- | --- |
| 0 | Single-sided (default) |
| 1 | Double-sided |
|  | X specifies the input time-domain signal. |
|  | Y specifies the input time-domain signal. |
|  | dt specifies the sample period of X and Y, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cross Power Spectrum Magnitude returns the magnitude of the cross power spectrum of signal X and Y. |
|  | Cross Power Spectrum Phase returns the phase spectrum, in radians, showing the difference between the phases of signal X and Y. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power Spectrum (SGL)

[IMAGE alt='image' src='cross_power_spectrum__sgl.gif']

|  | power spectrum type specifies whether the output Cross Power Spectrum is single-sided or double-sided. 0Single-sided (default)1Double-sided |
| --- | --- |
| 0 | Single-sided (default) |
| 1 | Double-sided |
|  | X specifies the input time-domain signal. |
|  | Y specifies the input time-domain signal. |
|  | dt specifies the sample period of X and Y, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cross Power Spectrum Magnitude returns the magnitude of the cross power spectrum of signal X and Y. |
|  | Cross Power Spectrum Phase returns the phase spectrum, in radians, showing the difference between the phases of signal X and Y. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power Spectrum (CSG)

[IMAGE alt='image' src='cross_power_spectrum__csg.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | dt specifies the sample period of X and Y, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cross Power Spectrum Magnitude returns the magnitude of the cross power spectrum of signal X and Y. |
|  | Cross Power Spectrum Phase returns the phase spectrum, in radians, showing the difference between the phases of signal X and Y. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power Spectrum (CDB)

[IMAGE alt='image' src='cross_power_spectrum__cdb.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | Y specifies the input time-domain signal. |
|  | dt specifies the sample period of X and Y, usually in seconds. Set dt to 1/fs, where fs is the sampling frequency of the time-domain signals. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Cross Power Spectrum Magnitude returns the magnitude of the cross power spectrum of signal X and Y. |
|  | Cross Power Spectrum Phase returns the phase spectrum, in radians, showing the difference between the phases of signal X and Y. |
|  | df returns the frequency interval of the power spectrum, in hertz, if dt is in seconds. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Cross Power Spectrum Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

If the input signals **X** and **Y** have different lengths, this VI first pads zeros to the shorter input signal to make the signals the same length. Let *n* represent the common length of the two signals after this VI pads zeros to the end of the shorter input signal.

This VI computes the double-sided cross power spectrum using the following equation.

[IMAGE alt='image' src='noloc_eq_dbl_cross_pwr_spectrum.gif']

where *P*<sub>double</sub> is the double-sided **Power Spectrum**.

To compute the single-sided cross power spectrum, this VI [converts the double-sided power spectrum to the single-sided form](/csh?topicname=lvanlsconcepts/lvac_convert_twosided_power_spec_to_singlesided.html).

Refer to the [Details](/csh?topicname=lvanls/cross_power_spectrum.html) section in the [Cross Power Spectrum](/csh?topicname=lvanls/cross_power_spectrum.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_dct.html language=enus -->
## TOPIC 00038: DCT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_dct.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_dct.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DCT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the Discrete Cosine Transform (DCT) of the input sequence **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D DCT (DBL)

[IMAGE alt='image' src='1d_dct__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DCT size specifies the length of DCT you want to perform. If DCT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of DCT size. If DCT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the DCT, where n is DCT size. If DCT size is less than or equal to 0, this VI uses the length of X as the DCT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DCT {X} returns the DCT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D DCT (SGL)

[IMAGE alt='image' src='1d_dct__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DCT size specifies the length of DCT you want to perform. If DCT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of DCT size. If DCT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the DCT, where n is DCT size. If DCT size is less than or equal to 0, this VI uses the length of X as the DCT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DCT {X} returns the DCT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D DCT (DBL)

[IMAGE alt='image' src='2d_dct__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DCT rows specifies the number of rows of the 2D DCT. This VI truncates or zero pads X to an m-by-n array before performing the DCT, where m is DCT rows and n is DCT columns. |
|  | DCT columns specifies the number of columns of the 2D DCT. This VI truncates or zero pads X to an m-by-n array before performing the DCT, where m is DCT rows and n is DCT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DCT {X} returns the DCT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D DCT (SGL)

[IMAGE alt='image' src='2d_dct__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DCT rows specifies the number of rows of the 2D DCT. This VI truncates or zero pads X to an m-by-n array before performing the DCT, where m is DCT rows and n is DCT columns. |
|  | DCT columns specifies the number of columns of the 2D DCT. This VI truncates or zero pads X to an m-by-n array before performing the DCT, where m is DCT rows and n is DCT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DCT {X} returns the DCT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DCT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/dct.html) section in the [DCT](/csh?topicname=lvanls/dct.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_dense_to_sparse.html language=enus -->
## TOPIC 00039: Dense to Sparse VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_dense_to_sparse.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_dense_to_sparse.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Dense to Sparse VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts a dense matrix to a sparse matrix that contains only nonzero elements.

Wire data to the **Dense Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Dense to Sparse (DBL)

[IMAGE alt='image' src='dense_to_sparse__dbl.gif']

|  | Dense Matrix specifies the input dense matrix to convert to a sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns the sparse matrix that this VI converts from Dense Matrix that contains only nonzero elements. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense to Sparse (SGL)

[IMAGE alt='image' src='dense_to_sparse__sgl.gif']

|  | Dense Matrix specifies the input dense matrix to convert to a sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns the sparse matrix that this VI converts from Dense Matrix that contains only nonzero elements. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense to Sparse (CDB)

[IMAGE alt='image' src='dense_to_sparse__cdb.gif']

|  | Dense Matrix specifies the input dense matrix to convert to a sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns the sparse matrix that this VI converts from Dense Matrix that contains only nonzero elements. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense to Sparse (CSG)

[IMAGE alt='image' src='dense_to_sparse__csg.gif']

|  | Dense Matrix specifies the input dense matrix to convert to a sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns the sparse matrix that this VI converts from Dense Matrix that contains only nonzero elements. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dense to Sparse Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_determinant.html language=enus -->
## TOPIC 00040: Determinant VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_determinant.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_determinant.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Determinant VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the determinant of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Determinant (DBL)

[IMAGE alt='image' src='determinant__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets determinant to NaN. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the determinant and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | determinant returns the determinant of Input Matrix. If Input Matrix is singular, determinant is 0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Determinant (SGL)

[IMAGE alt='image' src='determinant__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets determinant to NaN. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the determinant and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | determinant returns the determinant of Input Matrix. If Input Matrix is singular, determinant is 0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Determinant (CDB)

[IMAGE alt='image' src='determinant__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets determinant to NaN + NaNi. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the determinant and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | determinant returns the determinant of Input Matrix. If Input Matrix is singular, determinant is 0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Determinant (CSG)

[IMAGE alt='image' src='determinant__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets determinant to NaN + NaNi. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the determinant and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | determinant returns the determinant of Input Matrix. If Input Matrix is singular, determinant is 0. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Determinant Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following cases are exceptions: Determinant (DBL) when matrix type is General or Positive Definite Determinant (CSG) when matrix type is Positive Definite |

Refer to the [Details](/csh?topicname=gmath/determinant.html) section in the [Determinant](/csh?topicname=gmath/determinant.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_dot_product.html language=enus -->
## TOPIC 00041: Dot Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_dot_product.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_dot_product.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Dot Product VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the dot product of **X Vector** and **Y Vector**.

Wire data to the **X Vector** and **Y Vector** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Dot Product (DBL)

[IMAGE alt='image' src='dot_product__dbl.gif']

|  | X Vector specifies the first input vector. The number of elements in X Vector must be equal to the number of elements in Y Vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X * Y returns the dot product of X Vector and Y Vector. If either X Vector or Y Vector is empty, or the number of elements in X Vector is different from the number of elements in Y Vector, the dot product is undefined and X * Y is set to NaN. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dot Product (SGL)

[IMAGE alt='image' src='dot_product__sgl.gif']

|  | X Vector specifies the first input vector. The number of elements in X Vector must be equal to the number of elements in Y Vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X * Y returns the dot product of X Vector and Y Vector. If either X Vector or Y Vector is empty, or the number of elements in X Vector is different from the number of elements in Y Vector, the dot product is undefined and X * Y is set to NaN. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dot Product (CDB)

[IMAGE alt='image' src='dot_product__cdb.gif']

|  | X Vector specifies the first input vector. The number of elements in X Vector must be equal to the number of elements in Y Vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X * Y returns the dot product of X Vector and Y Vector. If either X Vector or Y Vector is empty, or the number of elements in X Vector is different from the number of elements in Y Vector, the dot product is undefined and X * Y is set to NaN + NaNi. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dot Product (CSG)

[IMAGE alt='image' src='dot_product__csg.gif']

|  | X Vector specifies the first input vector. The number of elements in X Vector must be equal to the number of elements in Y Vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X * Y returns the dot product of X Vector and Y Vector. If either X Vector or Y Vector is empty, or the number of elements in X Vector is different from the number of elements in Y Vector, the dot product is undefined and X * Y is set to NaN + NaNi. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Dot Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/dot_product.html) section in the [Dot Product](/csh?topicname=gmath/dot_product.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_draw_sparse_graph.html language=enus -->
## TOPIC 00042: Draw Sparse Graph VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_draw_sparse_graph.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_draw_sparse_graph.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Draw Sparse Graph VI

**Owning Palette:** [Visualization VIs](../lvmasmtref/masm_visualization_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Treats the sparse matrix as an adjacency matrix and draws the graph.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### Draw Sparse Graph (DBL)

[IMAGE alt='image' src='draw_sparse_graph__dbl.gif']

|  | Labels specifies the label strings to display at each vertex. The number of elements in Labels must be equal to the number of rows and columns in Sparse Matrix. By default, LabVIEW does not display any label strings. |
| --- | --- |
|  | Sparse Matrix specifies a square sparse matrix to draw. |
|  | X specifies the x-coordinate for each vertex. The number of elements in X must be equal to the number of rows and columns in Sparse Matrix. |
|  | Y specifies the y-coordinate for each vertex. The number of elements in Y must be equal to the number of rows and columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Z specifies the z-coordinate for each vertex. The number of elements in Z must be equal to the number of rows and columns in Sparse Matrix. By default, LabVIEW assumes the values of Z are zeros. |
|  | Sparse Graph Plot returns a reference to a 3D scene object. Wire this output to the 3D picture control to view the graph of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Graph (SGL)

[IMAGE alt='image' src='draw_sparse_graph__sgl.gif']

|  | Labels specifies the label strings to display at each vertex. The number of elements in Labels must be equal to the number of rows and columns in Sparse Matrix. By default, LabVIEW does not display any label strings. |
| --- | --- |
|  | Sparse Matrix specifies a square sparse matrix to draw. |
|  | X specifies the x-coordinate for each vertex. The number of elements in X must be equal to the number of rows and columns in Sparse Matrix. |
|  | Y specifies the y-coordinate for each vertex. The number of elements in Y must be equal to the number of rows and columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Z specifies the z-coordinate for each vertex. The number of elements in Z must be equal to the number of rows and columns in Sparse Matrix. By default, LabVIEW assumes the values of Z are zeros. |
|  | Sparse Graph Plot returns a reference to a 3D scene object. Wire this output to the 3D picture control to view the graph of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Graph Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | No |
| --- | --- |

An adjacency matrix is the matrix representation of a graph. The *n*-by-*n* adjacency matrix corresponds to a graph on *n* vertices. The matrix element at the (*i*, *j*) position corresponds to the graph edge from vertices *i* to *j*. A zero matrix element usually means that no connection exists between two vertices.

The following figure shows a graph with six vertices and 11 edges.

[IMAGE alt='image' src='noloc_eps_adj_matrix_graph.gif']

Suppose that the edges in the graph are undirected and not weighted. The following symmetric matrix illustrates the corresponding adjacent matrix.

[IMAGE alt='image' src='noloc_adj_matrix.gif']

#### Example

Refer to the Visualize Sparse Matrices VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Draw Sparse Graph VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_draw_sparse_pattern.html language=enus -->
## TOPIC 00043: Draw Sparse Pattern VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_draw_sparse_pattern.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_draw_sparse_pattern.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Draw Sparse Pattern VI

**Owning Palette:** [Visualization VIs](../lvmasmtref/masm_visualization_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Draws the pattern of elements in a sparse matrix. The pattern shows the coordinates, the row and column indices, of elements in the sparse matrix. This VI ignores the actual values of elements in the sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### Draw Sparse Pattern (DBL)

[IMAGE alt='image' src='draw_sparse_pattern__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Pattern Plot returns an XY graph that shows the pattern of elements in Sparse Matrix. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Pattern (SGL)

[IMAGE alt='image' src='draw_sparse_pattern__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Pattern Plot returns an XY graph that shows the pattern of elements in Sparse Matrix. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Pattern (CDB)

[IMAGE alt='image' src='draw_sparse_pattern__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Pattern Plot returns an XY graph that shows the pattern of elements in Sparse Matrix. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Pattern (CSG)

[IMAGE alt='image' src='draw_sparse_pattern__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Pattern Plot returns an XY graph that shows the pattern of elements in Sparse Matrix. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Pattern Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

#### Example

Refer to the Visualize Sparse Matrices VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Draw Sparse Pattern VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_draw_sparse_structure.html language=enus -->
## TOPIC 00044: Draw Sparse Structure VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_draw_sparse_structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_draw_sparse_structure.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Draw Sparse Structure VI

**Owning Palette:** [Visualization VIs](../lvmasmtref/masm_visualization_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Draws the structure of elements in a sparse matrix. The structure shows not only the coordinates, the row and column indices, of elements, but also the actual values of elements in the sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### Draw Sparse Structure (DBL)

[IMAGE alt='image' src='draw_sparse_structure__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Structure Plot returns a reference to a 3D scene object. Wire this output to the 3D picture control to view the structure of elements in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Structure (SGL)

[IMAGE alt='image' src='draw_sparse_structure__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Structure Plot returns a reference to a 3D scene object. Wire this output to the 3D picture control to view the structure of elements in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Draw Sparse Structure Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | No |
| --- | --- |

#### Example

Refer to the Visualize Sparse Matrices VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Draw Sparse Structure VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_dst.html language=enus -->
## TOPIC 00045: DST VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_dst.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_dst.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### DST VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the Discrete Sine Transform (DST) of the input sequence **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D DST (DBL)

[IMAGE alt='image' src='1d_dst__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DST size is the length of the DST you want to perform. If DST size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of DST size. If DST size is less than the number of elements in X, this VI uses only the first n elements in X to perform the DST, where n is DST size. If DST size is less than or equal to zero, this VI uses the length of X as the DST size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DST {X} returns the DST of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D DST (SGL)

[IMAGE alt='image' src='1d_dst__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DST size is the length of the DST you want to perform. If DST size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of DST size. If DST size is less than the number of elements in X, this VI uses only the first n elements in X to perform the DST, where n is DST size. If DST size is less than or equal to zero, this VI uses the length of X as the DST size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DST {X} returns the DST of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D DST (DBL)

[IMAGE alt='image' src='2d_dst__dbl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DST rows specifies the number of rows of the 2D DST. This VI truncates or zero pads X to an m-by-n array before performing the DST, where m is DST rows and n is DST columns. |
|  | DST columns specifies the number of columns of the 2D DST. This VI truncates or zero pads X to an m-by-n array before performing the DST, where m is DST rows and n is DST columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DST {X} returns the DST of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D DST (SGL)

[IMAGE alt='image' src='2d_dst__sgl.gif']

|  | X specifies the input sequence. |
| --- | --- |
|  | DST rows specifies the number of rows of the 2D DST. This VI truncates or zero pads X to an m-by-n array before performing the DST, where m is DST rows and n is DST columns. |
|  | DST columns specifies the number of columns of the 2D DST. This VI truncates or zero pads X to an m-by-n array before performing the DST, where m is DST rows and n is DST columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | DST {X} returns the DST of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DST Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/dst.html) section in the [DST](/csh?topicname=lvanls/dst.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_eigenvalues_vectors.html language=enus -->
## TOPIC 00046: Eigenvalues and Vectors VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_eigenvalues_vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_eigenvalues_vectors.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Eigenvalues and Vectors VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Finds the eigenvalues and right eigenvectors of the square **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Eigenvalues and Vectors (DBL)

[IMAGE alt='image' src='eigenvalues_and_vectors__dbl.gif']

|  | Input Matrix specifies an n-by-n square matrix, where n is the number of rows and columns of Input Matrix. |
| --- | --- |
|  | matrix type is the type of Input Matrix. A symmetric matrix always has real eigenvectors and eigenvalues. 0General (default)1Symmetric |
| 0 | General (default) |
| 1 | Symmetric |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns a complex vector of n elements, which contains all of the computed eigenvalues of the Input Matrix. The eigenvalues are all real if matrix type is set to Symmetric. |
|  | Eigenvectors returns an n-by-n complex matrix containing all of the computed Eigenvectors of the Input Matrix. The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1. The eigenvectors are all real if matrix type is set to Symmetric. If output option is set to Eigenvalues, this VI returns Eigenvectors as an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eigenvalues and Vectors (SGL)

[IMAGE alt='image' src='eigenvalues_and_vectors__sgl.gif']

|  | Input Matrix specifies an n-by-n square matrix, where n is the number of rows and columns of Input Matrix. |
| --- | --- |
|  | matrix type is the type of Input Matrix. A symmetric matrix always has real eigenvectors and eigenvalues. 0General (default)1Symmetric |
| 0 | General (default) |
| 1 | Symmetric |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns a complex vector of n elements, which contains all of the computed eigenvalues of the Input Matrix. The eigenvalues are all real if matrix type is set to Symmetric. |
|  | Eigenvectors returns an n-by-n complex matrix containing all of the computed Eigenvectors of the Input Matrix. The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1. The eigenvectors are all real if matrix type is set to Symmetric. If output option is set to Eigenvalues, this VI returns Eigenvectors as an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eigenvalues and Vectors (CDB)

[IMAGE alt='image' src='eigenvalues_and_vectors__cdb.gif']

|  | Input Matrix specifies an n-by-n square matrix, where n is the number of rows and columns of Input Matrix. |
| --- | --- |
|  | matrix type is the type of Input Matrix. A Hermitian matrix always has real eigenvalues. 0General (default)1Hermitian |
| 0 | General (default) |
| 1 | Hermitian |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns a complex vector of n elements, which contains all of the computed eigenvalues of the Input Matrix. The eigenvalues are all real if matrix type is set to Hermitian. |
|  | Eigenvectors returns an n-by-n complex matrix containing all of the computed Eigenvectors of the Input Matrix. The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1. If output option is set to Eigenvalues, this VI returns Eigenvectors as an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eigenvalues and Vectors (CSG)

[IMAGE alt='image' src='eigenvalues_and_vectors__csg.gif']

|  | Input Matrix specifies an n-by-n square matrix, where n is the number of rows and columns of Input Matrix. |
| --- | --- |
|  | matrix type is the type of Input Matrix. A Hermitian matrix always has real eigenvalues. 0General (default)1Hermitian |
| 0 | General (default) |
| 1 | Hermitian |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns a complex vector of n elements, which contains all of the computed eigenvalues of the Input Matrix. The eigenvalues are all real if matrix type is set to Hermitian. |
|  | Eigenvectors returns an n-by-n complex matrix containing all of the computed Eigenvectors of the Input Matrix. The ith column of Eigenvectors is the eigenvector corresponding to the ith component of the vector, Eigenvalues. Each eigenvector is normalized so that its Euclidean norm equals 1. If output option is set to Eigenvalues, this VI returns Eigenvectors as an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Eigenvalues and Vectors Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following cases are exceptions: Eigenvalues and Vectors (DBL) when matrix type is Symmetric Eigenvalues and Vectors (CSG) when matrix type is Hermitian |

Refer to the [Details](/csh?topicname=gmath/eigenvalues_and_vectors.html) section in the [Eigenvalues and Vectors](/csh?topicname=gmath/eigenvalues_and_vectors.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_equal.html language=enus -->
## TOPIC 00047: Equal VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_equal.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Equal VI

**Owning Palette:** [Comparison VIs](../lvmasmtref/masm_comparison_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Returns TRUE if two sparse matrices are equal. Otherwise, this VI returns FALSE.

Two matrices are equal if and only if they have the same size and all corresponding elements have the same values.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Equal Sparse Matrix (DBL)

[IMAGE alt='image' src='equal_sparse_matrix__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A = B? returns TRUE if A is equal to B. Otherwise, returns FALSE. |

#### Equal Sparse Matrix (SGL)

[IMAGE alt='image' src='equal_sparse_matrix__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A = B? returns TRUE if A is equal to B. Otherwise, returns FALSE. |

#### Equal Sparse Matrix (CDB)

[IMAGE alt='image' src='equal_sparse_matrix__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A = B? returns TRUE if A is equal to B. Otherwise, returns FALSE. |

#### Equal Sparse Matrix (CSG)

[IMAGE alt='image' src='equal_sparse_matrix__csg.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A = B? returns TRUE if A is equal to B. Otherwise, returns FALSE. |

#### Equal Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_equal_to_zero.html language=enus -->
## TOPIC 00048: Equal to Zero VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_equal_to_zero.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_equal_to_zero.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Equal to Zero VI

**Owning Palette:** [Comparison VIs](../lvmasmtref/masm_comparison_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Returns TRUE if **Sparse Matrix** is a zero matrix. Otherwise, this VI returns FALSE.

A matrix is a zero matrix if and only if it is empty or all its elements are zeros.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Equal to Zero Sparse Matrix (DBL)

[IMAGE alt='image' src='equal_to_zero_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | zero matrix? returns TRUE if Sparse Matrix is a zero matrix. Otherwise, returns FALSE. |

#### Equal to Zero Sparse Matrix (SGL)

[IMAGE alt='image' src='equal_to_zero_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | zero matrix? returns TRUE if Sparse Matrix is a zero matrix. Otherwise, returns FALSE. |

#### Equal to Zero Sparse Matrix (CDB)

[IMAGE alt='image' src='equal_to_zero_sparse_matrix__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | zero matrix? returns TRUE if Sparse Matrix is a zero matrix. Otherwise, returns FALSE. |

#### Equal to Zero Sparse Matrix (CSG)

[IMAGE alt='image' src='equal_to_zero_sparse_matrix__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | zero matrix? returns TRUE if Sparse Matrix is a zero matrix. Otherwise, returns FALSE. |

#### Equal to Zero Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_fft.html language=enus -->
## TOPIC 00049: FFT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_fft.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### FFT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the fast Fourier transform (FFT) of the input sequence **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D FFT (DBL)

[IMAGE alt='image' src='1d_fft__dbl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT size specifies the length of the FFT you want to perform. If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI uses the length of X as the FFT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D FFT (SGL)

[IMAGE alt='image' src='1d_fft__sgl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT size specifies the length of the FFT you want to perform. If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI uses the length of X as the FFT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D FFT (CDB)

[IMAGE alt='image' src='1d_fft__cdb.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT size specifies the length of the FFT you want to perform. If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI uses the length of X as the FFT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D FFT (CSG)

[IMAGE alt='image' src='1d_fft__csg.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT size specifies the length of the FFT you want to perform. If FFT size is greater than the number of elements in X, this VI adds zeros to the end of X to match the size of FFT size. If FFT size is less than the number of elements in X, this VI uses only the first n elements in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI uses the length of X as the FFT size. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D FFT (DBL)

[IMAGE alt='image' src='2d_fft__dbl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D FFT (SGL)

[IMAGE alt='image' src='2d_fft__sgl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D FFT (CDB)

[IMAGE alt='image' src='2d_fft__cdb.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D FFT (CSG)

[IMAGE alt='image' src='2d_fft__csg.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 2D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D FFT (DBL)

[IMAGE alt='image' src='3d_fft__dbl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | Xspecifies the input sequence. |
|  | FFT rows specifies the number of rows of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT pages specifies the number of pages of the 3D FFT. This VI truncates or zero pads X to an m-by-n-by-k array before performing the FFT, where m is FFT rows, n is FFT columns, and k is FFT pages. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D FFT (SGL)

[IMAGE alt='image' src='3d_fft__sgl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT pages specifies the number of pages of the 3D FFT. This VI truncates or zero pads X to an m-by-n-by-k array before performing the FFT, where m is FFT rows, n is FFT columns, and k is FFT pages. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D FFT (CDB)

[IMAGE alt='image' src='3d_fft__cdb.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT pages specifies the number of pages of the 3D FFT. This VI truncates or zero pads X to an m-by-n-by-k array before performing the FFT, where m is FFT rows, n is FFT columns, and k is FFT pages. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D FFT (CSG)

[IMAGE alt='image' src='3d_fft__csg.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | X specifies the input sequence. |
|  | FFT rows specifies the number of rows of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT columns specifies the number of columns of the 3D FFT. This VI truncates or zero pads X to an m-by-n array before performing the FFT, where m is FFT rows and n is FFT columns. |
|  | FFT pages specifies the number of pages of the 3D FFT. This VI truncates or zero pads X to an m-by-n-by-k array before performing the FFT, where m is FFT rows, n is FFT columns, and k is FFT pages. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT {X} returns the FFT of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### FFT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/fft.html) section in the [FFT](/csh?topicname=lvanls/fft.html) VI for more details about the 1D and 2D instances of this VI.

##### 3D FFT

For 3D signals, this VI computes the discrete Fourier transform (DFT) of the input 3D array. The following equation defines the DFT of an *M*-by-*N*-by-*K* array:

[IMAGE alt='image' src='noloc_eq_3d_dft.gif']

for *u* = 0, 1, … *M*–1; *v*=0, 1, …, *N*–1; *w*=0, 1, …, *K*–1.

where *X* is the input signal and *Y* is the transform result.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_file_vis.html language=enus -->
## TOPIC 00050: File I/O VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_file_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_file_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### File I/O VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the File I/O VIs to read from and write to a file in the Matrix Market exchange format.

| Palette Object | Description |
| --- | --- |
| Read from Matrix Market File | Reads a matrix from a file in the Matrix Market exchange format. |
| Write to Matrix Market File | Writes a matrix into a file in the Matrix Market exchange format. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_gemm.html language=enus -->
## TOPIC 00051: gemm - General Matrix-Matrix Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_gemm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_gemm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### gemm - General Matrix-Matrix Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of two general matrices.

Wire data to the **A**, **B**, and **C** inputs to determine the polymorphic instance to use.

[Details](#details)

#### dgemm - General Matrix-Matrix Product (DBL)

[IMAGE alt='image' src='dgemm_-_general_matrix-matrix_product__dbl.gif']

|  | operation B specifies the operation this VI performs on matrix B that results in matrix op(B). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions M x K. |
|  | B specifies a matrix such that op(B) has dimensions K x N. |
|  | C specifies a matrix of dimensions greater than or equal to M x N. The default is an M x N zero matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*op(B). The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | dgemm returns a matrix of the same size as C. For elements of the first M rows and N columns, this VI returns the result of alpha*op(A)*op(B) + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### sgemm - General Matrix-Matrix Product (SGL)

[IMAGE alt='image' src='sgemm_-_general_matrix-matrix_product__sgl.gif']

|  | operation B specifies the operation this VI performs on matrix B that results in matrix op(B). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions M x K. |
|  | B specifies a matrix such that op(B) has dimensions K x N. |
|  | C specifies a matrix of dimensions greater than or equal to M x N. The default is an M x N zero matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*op(B). The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | sgemm returns a matrix of the same size as C. For elements of the first M rows and N columns, this VI returns the result of alpha*op(A)*op(B) + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### zgemm - General Matrix-Matrix Product (CDB)

[IMAGE alt='image' src='zgemm_-_general_matrix-matrix_product__cdb.gif']

|  | operation B specifies the operation this VI performs on matrix B that results in matrix op(B). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions M x K. |
|  | B specifies a matrix such that op(B) has dimensions K x N. |
|  | C specifies a matrix of dimensions greater than or equal to M x N. The default is an M x N zero matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*op(B). The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | zgemm returns a matrix of the same size as C. For elements of the first M rows and N columns, this VI returns the result of alpha*op(A)*op(B) + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### cgemm - General Matrix-Matrix Product (CSG)

[IMAGE alt='image' src='cgemm_-_general_matrix-matrix_product__csg.gif']

|  | operation B specifies the operation this VI performs on matrix B that results in matrix op(B). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions M x K. |
|  | B specifies a matrix such that op(B) has dimensions K x N. |
|  | C specifies a matrix of dimensions greater than or equal to M x N. The default is an M x N zero matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*op(B). The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | cgemm returns a matrix of the same size as C. For elements of the first M rows and N columns, this VI returns the result of alpha*op(A)*op(B) + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### gemm - General Matrix-Matrix Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_gemv.html language=enus -->
## TOPIC 00052: gemv - General Matrix-Vector Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_gemv.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_gemv.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### gemv - General Matrix-Vector Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a general matrix and a vector.

Wire data to the **A**, **x**, and **y** inputs to determine the polymorphic instance to use.

[Details](#details)

#### dgemv - General Matrix-Vector Product (DBL)

[IMAGE alt='image' src='dgemv_-_general_matrix-vector_product__dbl.gif']

|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions N x M. |
|  | x specifies a vector. This VI multiplies the first M elements in x by op(A). x must have at least M elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | dgemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*op(A)*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### sgemv - General Matrix-Vector Product (SGL)

[IMAGE alt='image' src='sgemv_-_general_matrix-vector_product__sgl.gif']

|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions N x M. |
|  | x specifies a vector. This VI multiplies the first M elements in x by op(A). x must have at least M elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | sgemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*op(A)*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### zgemv - General Matrix-Vector Product (CDB)

[IMAGE alt='image' src='zgemv_-_general_matrix-vector_product__cdb.gif']

|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions N x M. |
|  | x specifies a vector. This VI multiplies the first M elements in x by op(A). x must have at least M elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*x. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | zgemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*op(A)*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### cgemv - General Matrix-Vector Product (CSG)

[IMAGE alt='image' src='cgemv_-_general_matrix-vector_product__csg.gif']

|  | operation A specifies the operation this VI performs on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a matrix such that op(A) has dimensions N x M. |
|  | x specifies a vector. This VI multiplies the first M elements in x by op(A). x must have at least M elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales op(A)*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | cgemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*op(A)*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### gemv - General Matrix-Vector Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_gen_eigenvalues_vectors.html language=enus -->
## TOPIC 00053: Generalized Eigenvalues and Vectors VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_gen_eigenvalues_vectors.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_gen_eigenvalues_vectors.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Generalized Eigenvalues and Vectors VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the generalized eigenvalue and eigenvectors of a pair of matrices **A** and **B**.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Generalized Eigenvalues and Vectors (DBL)

[IMAGE alt='image' src='generalized_eigenvalues_and_vectors__dbl.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns the generalized eigenvalues of matrix pair (A,B). |
|  | Eigenvectors returns the complex matrix that contains the generalized right eigenvectors in its columns. Eigenvectors is empty if output option is Eigenvalues. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generalized Eigenvalues and Vectors (SGL)

[IMAGE alt='image' src='generalized_eigenvalues_and_vectors__sgl.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns the generalized eigenvalues of matrix pair (A,B). |
|  | Eigenvectors returns the complex matrix that contains the generalized right eigenvectors in its columns. Eigenvectors is empty if output option is Eigenvalues. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generalized Eigenvalues and Vectors (CDB)

[IMAGE alt='image' src='generalized_eigenvalues_and_vectors__cdb.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns the generalized eigenvalues of matrix pair (A,B). |
|  | Eigenvectors returns the complex matrix that contains the generalized right eigenvectors in its columns. Eigenvectors is empty if output option is Eigenvalues. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generalized Eigenvalues and Vectors (CSG)

[IMAGE alt='image' src='generalized_eigenvalues_and_vectors__csg.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | output option specifies whether this VI computes eigenvectors and/or eigenvalues. 0Eigenvalues—Specifies to compute eigenvalues only.1Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
| 0 | Eigenvalues—Specifies to compute eigenvalues only. |
| 1 | Eigenvalues & Vectors (default)—Specifies to compute eigenvalues and eigenvectors. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvalues returns the generalized eigenvalues of matrix pair (A,B). |
|  | Eigenvectors returns the complex matrix that contains the generalized right eigenvectors in its columns. Eigenvectors is empty if output option is Eigenvalues. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Generalized Eigenvalues and Vectors Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_get_matrix_size.html language=enus -->
## TOPIC 00054: Get Matrix Size VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_get_matrix_size.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_get_matrix_size.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Matrix Size VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Returns the number of rows and columns in a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### Get Sparse Matrix Size (DBL)

[IMAGE alt='image' src='get_sparse_matrix_size__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Size (SGL)

[IMAGE alt='image' src='get_sparse_matrix_size__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Size (CDB)

[IMAGE alt='image' src='get_sparse_matrix_size__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Size (CSG)

[IMAGE alt='image' src='get_sparse_matrix_size__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Matrix Size Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

#### Example

Refer to the Sparse Matrix Attributes and Subsets VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Get Matrix Size VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_get_matrix_storage_form.html language=enus -->
## TOPIC 00055: Get Matrix Storage Format VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_get_matrix_storage_form.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_get_matrix_storage_form.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Matrix Storage Format VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Gets the storage format of a sparse matrix.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)  [Example](#examples)

#### Get Sparse Matrix COO (DBL)

[IMAGE alt='image' src='get_sparse_matrix_coo__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in the coordinate format according to their row and column indices. 0No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order.1Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices.2Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices.3Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices. |
| 3 | Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the coordinate format. |
|  | Column Indices returns the column indices of elements in the coordinate format. |
|  | Elements returns the values of the elements in the coordinate format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix COO (SGL)

[IMAGE alt='image' src='get_sparse_matrix_coo__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in the coordinate format according to their row and column indices. 0No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order.1Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices.2Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices.3Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices. |
| 3 | Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the coordinate format. |
|  | Column Indices returns the column indices of elements in the coordinate format. |
|  | Elements returns the values of the elements in the coordinate format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix COO (CDB)

[IMAGE alt='image' src='get_sparse_matrix_coo__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in the coordinate format according to their row and column indices. 0No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order.1Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices.2Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices.3Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices. |
| 3 | Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the coordinate format. |
|  | Column Indices returns the column indices of elements in the coordinate format. |
|  | Elements returns the values of the elements in the coordinate format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix COO (CSG)

[IMAGE alt='image' src='get_sparse_matrix_coo__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in the coordinate format according to their row and column indices. 0No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order.1Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices.2Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices.3Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder (default)—Specifies that this VI does not reorder elements in the coordinate format in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices. |
| 3 | Row and Column—Specifies that this VI reorders elements in the coordinate format in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in the coordinate format in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the coordinate format. |
|  | Column Indices returns the column indices of elements in the coordinate format. |
|  | Elements returns the values of the elements in the coordinate format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSR (DBL)

[IMAGE alt='image' src='get_sparse_matrix_csr__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Compressed Row Indices returns the compressed row indices of elements in the compressed sparse row format. |
|  | Column Indices returns the column indices of elements in the compressed sparse row format. |
|  | Elements returns the values of the elements in the compressed sparse row format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSR (SGL)

[IMAGE alt='image' src='get_sparse_matrix_csr__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Compressed Row Indices returns the compressed row indices of elements in the compressed sparse row format. |
|  | Column Indices returns the column indices of elements in the compressed sparse row format. |
|  | Elements returns the values of the elements in the compressed sparse row format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSR (CDB)

[IMAGE alt='image' src='get_sparse_matrix_csr__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Compressed Row Indices returns the compressed row indices of elements in the compressed sparse row format. |
|  | Column Indices returns the column indices of elements in the coordinate format. |
|  | Elements returns the values of the elements in the compressed sparse row format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSR (CSG)

[IMAGE alt='image' src='get_sparse_matrix_csr__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Compressed Row Indices returns the compressed row indices of elements in the compressed sparse row format. |
|  | Column Indices returns the column indices of elements in the compressed sparse row format. |
|  | Elements returns the values of the elements in the compressed sparse row format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSC (DBL)

[IMAGE alt='image' src='get_sparse_matrix_csc__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the compressed sparse column format. |
|  | Compressed Column Indices returns the compressed column indices of elements in the compressed sparse column format. |
|  | Elements returns the values of the elements in the compressed sparse column format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSC (SGL)

[IMAGE alt='image' src='get_sparse_matrix_csc__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the compressed sparse column format. |
|  | Compressed Column Indices returns the compressed column indices of elements in the compressed sparse column format. |
|  | Elements returns the values of the elements in the compressed sparse column format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSC (CDB)

[IMAGE alt='image' src='get_sparse_matrix_csc__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the compressed sparse column format. |
|  | Compressed Column Indices returns the compressed column indices of elements in the compressed sparse column format. |
|  | Elements returns the values of the elements in the compressed sparse column format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix CSC (CSG)

[IMAGE alt='image' src='get_sparse_matrix_csc__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row Indices returns the row indices of elements in the compressed sparse column format. |
|  | Compressed Column Indices returns the compressed column indices of elements in the compressed sparse column format. |
|  | Elements returns the values of the elements in the compressed sparse column format. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Matrix Storage Format Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

#### Example

Refer to the Sparse Matrix Storage Formats VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Get Matrix Storage Format VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_get_matrix_subset.html language=enus -->
## TOPIC 00056: Get Matrix Subset VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_get_matrix_subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_get_matrix_subset.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Matrix Subset VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Gets a subset from a sparse matrix.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)  [Example](#examples)

#### Get Sparse Matrix Element (DBL)

[IMAGE alt='image' src='get_sparse_matrix_element__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index of the element to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix - 1. The default is 0. |
|  | column index specifies the column index of the element to get from Sparse Matrix. The column index must be in the range of 0 and the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | element returns the element at the row index and column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Element (SGL)

[IMAGE alt='image' src='get_sparse_matrix_element__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index of the element to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix - 1. The default is 0. |
|  | column index specifies the column index of the element to get from Sparse Matrix. The column index must be in the range of 0 and the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | element returns the element at the row index and column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Element (CDB)

[IMAGE alt='image' src='get_sparse_matrix_element__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index of the element to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix - 1. The default is 0. |
|  | column index specifies the column index of the element to get from Sparse Matrix. The column index must be in the range of 0 and the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | element returns the element at the row index and column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Element (CSG)

[IMAGE alt='image' src='get_sparse_matrix_element__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index of the element to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix - 1. The default is 0. |
|  | column index specifies the column index of the element to get from Sparse Matrix. The column index must be in the range of 0 and the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | element returns the element at the row index and column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Multi Elem (DBL)

[IMAGE alt='image' src='get_sparse_matrix_multi_elem__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies the row indices of multiple elements to get from Sparse Matrix. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must range from 0 to the number of rows in Sparse Matrix. |
|  | Column Indices specifies the column indices of multiple elements to get from Sparse Matrix. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must range from 0 to the number of columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Elements returns the elements at the Row Indices and Column Indices from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Multi Elem (SGL)

[IMAGE alt='image' src='get_sparse_matrix_multi_elem__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies the row indices of multiple elements to get from Sparse Matrix. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must range from 0 to the number of rows in Sparse Matrix. |
|  | Column Indices specifies the column indices of multiple elements to get from Sparse Matrix. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must range from 0 to the number of columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Elements returns the elements at the Row Indices and Column Indices from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Multi Elem (CDB)

[IMAGE alt='image' src='get_sparse_matrix_multi_elem__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies the row indices of multiple elements to get from Sparse Matrix. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must range from 0 to the number of rows in Sparse Matrix. |
|  | Column Indices specifies the column indices of multiple elements to get from Sparse Matrix. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must range from 0 to the number of columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Elements returns the elements at the Row Indices and Column Indices from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Multi Elem (CSG)

[IMAGE alt='image' src='get_sparse_matrix_multi_elem__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies the row indices of multiple elements to get from Sparse Matrix. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must range from 0 to the number of rows in Sparse Matrix. |
|  | Column Indices specifies the column indices of multiple elements to get from Sparse Matrix. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must range from 0 to the number of columns in Sparse Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Elements returns the elements at the Row Indices and Column Indices from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Row (DBL)

[IMAGE alt='image' src='get_sparse_matrix_row__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index of the row to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row returns the row at row index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Row (SGL)

[IMAGE alt='image' src='get_sparse_matrix_row__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index of the row to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row returns the row at row index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Row (CDB)

[IMAGE alt='image' src='get_sparse_matrix_row__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index of the row to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row returns the row at row index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Row (CSG)

[IMAGE alt='image' src='get_sparse_matrix_row__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index of the row to get from Sparse Matrix. The row index must be in the range of 0 and the number of rows in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Row returns the row at row index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Column (DBL)

[IMAGE alt='image' src='get_sparse_matrix_column__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index of the column to get from Sparse Matrix. The column index must be in the range from 0 to the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Column returns the column at column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Column (SGL)

[IMAGE alt='image' src='get_sparse_matrix_column__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index of the column to get from Sparse Matrix. The column index must be in the range from 0 to the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Column returns the column at column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Column (CDB)

[IMAGE alt='image' src='get_sparse_matrix_column__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index of the column to get from Sparse Matrix. The column index must be in the range from 0 to the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Column returns the column at column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix Column (CSG)

[IMAGE alt='image' src='get_sparse_matrix_column__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index of the column to get from Sparse Matrix. The column index must be in the range from 0 to the number of columns in Sparse Matrix. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Column returns the column at column index from Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Matrix Subset Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

#### Example

Refer to the Sparse Matrix Attributes and Subsets VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Get Matrix Subset VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_get_num_nonzeros.html language=enus -->
## TOPIC 00057: Get Number of Nonzeros VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_get_num_nonzeros.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_get_num_nonzeros.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Number of Nonzeros VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Returns the number of nonzeros and the maximum number of nonzeros in a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)  [Example](#examples)

#### Get Sparse Matrix NNZ (DBL)

[IMAGE alt='image' src='get_sparse_matrix_nnz__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of nonzeros returns the number of nonzeros in Sparse Matrix. |
|  | max number of nonzeros returns the maximum number of nonzeros in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix NNZ (SGL)

[IMAGE alt='image' src='get_sparse_matrix_nnz__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of nonzeros returns the number of nonzeros in Sparse Matrix. |
|  | max number of nonzeros returns the maximum number of nonzeros in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix NNZ (CDB)

[IMAGE alt='image' src='get_sparse_matrix_nnz__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of nonzeros returns the number of nonzeros in Sparse Matrix. |
|  | max number of nonzeros returns the maximum number of nonzeros in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Sparse Matrix NNZ (CSG)

[IMAGE alt='image' src='get_sparse_matrix_nnz__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of nonzeros returns the number of nonzeros in Sparse Matrix. |
|  | max number of nonzeros returns the maximum number of nonzeros in Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Number of Nonzeros Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

#### Example

Refer to the Sparse Matrix Attributes and Subsets VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Get Number of Nonzeros VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_get_num_threads.html language=enus -->
## TOPIC 00058: Get Number of Threads VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_get_num_threads.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_get_num_threads.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Number of Threads VI

**Owning Palette:** [Thread Management VIs](../lvmasmtref/masm_thread_mgmt.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Gets the maximum number of threads available for parallelism.

This VI is not available on real-time operating systems.

[Details](#details)

[IMAGE alt='image' src='get_number_of_threads.gif']

|  | function domain specifies the domain of functions for which the maximum number of threads is available. 0Default (default)—Gets the default maximum number of threads available to all functions.1Linear Algebra—Gets the maximum number of threads available to linear algebra functions.2Transform—Gets the maximum number of threads available to transform functions. |
| --- | --- |
| 0 | Default (default)—Gets the default maximum number of threads available to all functions. |
| 1 | Linear Algebra—Gets the maximum number of threads available to linear algebra functions. |
| 2 | Transform—Gets the maximum number of threads available to transform functions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | number of threads returns the maximum number of threads available for parallelism in function domain. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Number of Threads Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | No |
| --- | --- |

Refer to the [Details](../lvmasmtref/masm_set_num_threads.html#details) section in the [Set Number of Threads](../lvmasmtref/masm_set_num_threads.html) VI for more details about how to set the number of threads available for parallelism.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_hemm.html language=enus -->
## TOPIC 00059: hemm - Hermitian Matrix-Matrix Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_hemm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_hemm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### hemm - Hermitian Matrix-Matrix Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a Hermitian matrix and another matrix.

Wire data to the **A**, **B**, and **C** inputs to determine the polymorphic instance to use.

[Details](#details)

#### zhemm - Hermitian Matrix-Matrix Product (CDB)

[IMAGE alt='image' src='zhemm_-_hermitian_matrix-matrix_product__cdb.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a Hermitian matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by B. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*B or B*A. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | zhemm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the results of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |

#### chemm - Hermitian Matrix-Matrix Product (CSG)

[IMAGE alt='image' src='chemm_-_hermitian_matrix-matrix_product__csg.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a Hermitian matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by B. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to zero. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*B or B*A. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | chemm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the results of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |

#### hemm - Hermitian Matrix-Matrix Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_hemv.html language=enus -->
## TOPIC 00060: hemv - Hermitian Matrix-Vector Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_hemv.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_hemv.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### hemv - Hermitian Matrix-Vector Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a Hermitian matrix and a vector.

Wire data to the **A**, **x**, and **y** inputs to determine the polymorphic instance to use.

[Details](#details)

#### zhemv - Hermitian Matrix-Vector Product (CDB)

[IMAGE alt='image' src='zhemv_-_hermitian_matrix-vector_product__cdb.gif']

|  | A specifies a Hermitian matrix. This VI multiplies the first N rows and N columns of the triangular component of A that you select for matrix A type by x, where N is the number of elements in x. A must have at least N rows and N columns. |
| --- | --- |
|  | x specifies a vector with N elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | zhemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*A*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### chemv - Hermitian Matrix-Vector Product (CSG)

[IMAGE alt='image' src='chemv_-_hermitian_matrix-vector_product__csg.gif']

|  | A specifies a Hermitian matrix. This VI multiplies the first N rows and N columns of the triangular component of A that you select for matrix A type by x, where N is the number of elements in x. A must have at least N rows and N columns. |
| --- | --- |
|  | x specifies a vector with N elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | chemv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*A*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### hemv - Hermitian Matrix-Vector Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_init_matrix.html language=enus -->
## TOPIC 00061: Initialize Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_init_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_init_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Matrix VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Initializes a zero sparse matrix with the specified number of row and columns.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Initialize Sparse Matrix (DBL)

[IMAGE alt='image' src='initialize_sparse_matrix__dbl.gif']

|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be non-negative. |
| --- | --- |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be non-negative. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the maximum number of nonzeros automatically. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns a zero sparse matrix with number of rows and number of columns. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Sparse Matrix (SGL)

[IMAGE alt='image' src='initialize_sparse_matrix__sgl.gif']

|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be non-negative. |
| --- | --- |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be non-negative. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the maximum number of nonzeros automatically. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns a zero sparse matrix with number of rows and number of columns. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Sparse Matrix (CDB)

[IMAGE alt='image' src='initialize_sparse_matrix__cdb.gif']

|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be non-negative. |
| --- | --- |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be non-negative. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the maximum number of nonzeros automatically. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns a zero sparse matrix with number of rows and number of columns. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Sparse Matrix (CSG)

[IMAGE alt='image' src='initialize_sparse_matrix__csg.gif']

|  | number of rows specifies the number of rows in Sparse Matrix. The number of rows must be non-negative. |
| --- | --- |
|  | number of columns specifies the number of columns in Sparse Matrix. The number of columns must be non-negative. |
|  | max number of nonzeros specifies the maximum number of nonzeros in Sparse Matrix. If max number of nonzeros is negative, LabVIEW determines the maximum number of nonzeros automatically. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix returns a zero sparse matrix with number of rows and number of columns. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_inverse_dct.html language=enus -->
## TOPIC 00062: Inverse DCT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_inverse_dct.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_inverse_dct.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse DCT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the inverse Discrete Cosine Transform (DCT) of the input sequence **DCT {X}**.

Wire data to the **DCT {X}** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D Inverse DCT (DBL)

[IMAGE alt='image' src='1d_inverse_dct__dbl.gif']

|  | DCT {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DCT of DCT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Inverse DCT (SGL)

[IMAGE alt='image' src='1d_inverse_dct__sgl.gif']

|  | DCT {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DCT of DCT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse DCT (DBL)

[IMAGE alt='image' src='2d_inverse_dct__dbl.gif']

|  | DCT {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DCT of DCT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse DCT (SGL)

[IMAGE alt='image' src='2d_inverse_dct__sgl.gif']

|  | DCT {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DCT of DCT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse DCT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/inverse_dct.html) section in the [Inverse DCT](/csh?topicname=lvanls/inverse_dct.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_inverse_dst.html language=enus -->
## TOPIC 00063: Inverse DST VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_inverse_dst.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_inverse_dst.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse DST VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the inverse Discrete Sine Transform (DST) of the input sequence **DST {X}**.

Wire data to the **DST {X}** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 1D Inverse DST (DBL)

[IMAGE alt='image' src='1d_inverse_dst__dbl.gif']

|  | DST {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DST of DST {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse DST (SGL)

[IMAGE alt='image' src='2d_inverse_dst__sgl.gif']

|  | DST {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DST of DST {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse DST (DBL)

[IMAGE alt='image' src='2d_inverse_dst__dbl.gif']

|  | DST {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DST of DST {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Inverse DST (SGL)

[IMAGE alt='image' src='1d_inverse_dst__sgl.gif']

|  | DST {X} specifies the real input sequence. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse DST of DST {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse DST Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=lvanls/inverse_dst.html) section in the [Inverse DST](/csh?topicname=lvanls/inverse_dst.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_inverse_fft.html language=enus -->
## TOPIC 00064: Inverse FFT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_inverse_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_inverse_fft.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse FFT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the inverse fast Fourier transform (FFT) of the input sequence **X**.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### 1D Inverse FFT (DBL)

[IMAGE alt='image' src='1d_inverse_fft__dbl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric except for the first element. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Inverse FFT (SGL)

[IMAGE alt='image' src='1d_inverse_fft__sgl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric except for the first element. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse FFT (SGL)

[IMAGE alt='image' src='2d_inverse_fft__sgl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric except for the first row and column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse FFT (DBL)

[IMAGE alt='image' src='2d_inverse_fft__dbl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric except for the first row and column. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Inverse FFT (CSG)

[IMAGE alt='image' src='1d_inverse_fft__csg.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 1D Inverse FFT (CDB)

[IMAGE alt='image' src='1d_inverse_fft__cdb.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D Inverse FFT (SGL)

[IMAGE alt='image' src='3d_inverse_fft__sgl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D Inverse FFT (DBL)

[IMAGE alt='image' src='3d_inverse_fft__dbl.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence, which should be conjugated centrosymmetric. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse FFT (CSG)

[IMAGE alt='image' src='2d_inverse_fft__csg.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse FFT (CDB)

[IMAGE alt='image' src='2d_inverse_fft__cdb.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D Inverse FFT (CDB)

[IMAGE alt='image' src='3d_inverse_fft__cdb.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 3D Inverse FFT (CSG)

[IMAGE alt='image' src='3d_inverse_fft__csg.gif']

|  | shift? specifies whether the DC component is at the center of FFT {X}. The default is FALSE. |
| --- | --- |
|  | FFT {X} specifies the complex-valued input sequence. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | X returns the inverse FFT of FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse FFT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Use the DBL or SGL instance of this VI only if **FFT {X}** is the Fourier transform of a real time-domain signal. Otherwise, use the CDB or CSG instance.

For a 1D, *N*-sample, frequency domain sequence *Y*, the following equation defines the inverse discrete Fourier transform (IDFT):

[IMAGE alt='image' src='noloc_eq_1d_inverse_fft.gif']

for *n*=0, 1, …, *N*–1.

For a 2D, *M*-by-*N* frequency domain sequence *Y*, the following equation defines the inverse discrete Fourier transform (IDFT):

[IMAGE alt='image' src='noloc_eq_2d_inverse_fft.gif']

for *m* = 0, 1, …, *M*–1, *n*=0, 1, …, *N*–1.

For a 3D, *M*-by-*N*-by-*K* frequency domain sequence *Y*, the following equation defines the inverse discrete Fourier transform (IDFT):

[IMAGE alt='image' src='noloc_eq_3d_inverse_fft.gif']

for *m* = 0, 1, …, *M*–1, *n*=0, 1, …, *N*–1, *k*=0, 1, …, *K*–1.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_inverse_matrix.html language=enus -->
## TOPIC 00065: Inverse Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_inverse_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_inverse_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse Matrix VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Finds the inverse, if it exists, of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Inverse Matrix (DBL)

[IMAGE alt='image' src='inverse_matrix__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty or singular, this VI sets Inverse Matrix to an empty matrix. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the inverse and can help you avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Inverse Matrix returns the inverse of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Matrix (SGL)

[IMAGE alt='image' src='inverse_matrix__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty or singular, this VI sets Inverse Matrix to an empty matrix. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the inverse and can help you avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Inverse Matrix returns the inverse of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Matrix (CDB)

[IMAGE alt='image' src='inverse_matrix__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty or singular, this VI sets Inverse Matrix to an empty matrix. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the inverse and can help you avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Inverse Matrix returns the inverse of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Matrix (CSG)

[IMAGE alt='image' src='inverse_matrix__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty or singular, this VI sets Inverse Matrix to an empty matrix. |
| --- | --- |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the inverse and can help you avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Inverse Matrix returns the inverse of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following cases are exceptions: Inverse Matrix (DBL) when matrix type is General or Positive Definite Inverse Matrix (CSG) when matrix type is Positive Definite |

Refer to the [Details](/csh?topicname=gmath/inverse_matrix.html) section in the [Inverse Matrix](/csh?topicname=gmath/inverse_matrix.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_inverse_multichannel_fft.html language=enus -->
## TOPIC 00066: Inverse Multi-channel FFT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_inverse_multichannel_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_inverse_multichannel_fft.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Inverse Multi-channel FFT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the inverse fast Fourier transform (IFFT) of the frequency-domain sequence in each channel in **Multi-channel FFT {X}**.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### 2D Inverse Multi-channel FFT (DBL)

[IMAGE alt='image' src='2d_inverse_multi-channel_fft__dbl.gif']

|  | shift? specifies whether the DC component is at the center of each channel of Multi-channel FFT {X}. The default is FALSE. |
| --- | --- |
|  | Multi-channel FFT {X} specifies frequency-domain sequences by rows or columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform inverse FFT on each row of Multi-channel FFT {X} or each column of Multi-channel FFT {X}. 0Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}.1Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
| 0 | Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}. |
| 1 | Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
|  | X returns the inverse FFT result of each channel in Multi-channel FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse Multi-channel FFT (SGL)

[IMAGE alt='image' src='2d_inverse_multi-channel_fft__sgl.gif']

|  | shift? specifies whether the DC component is at the center of each channel of Multi-channel FFT {X}. The default is FALSE. |
| --- | --- |
|  | Multi-channel FFT {X} specifies frequency-domain sequences by rows or columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform inverse FFT on each row of Multi-channel FFT {X} or each column of Multi-channel FFT {X}. 0Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}.1Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
| 0 | Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}. |
| 1 | Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
|  | X returns the inverse FFT result of each channel in Multi-channel FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse Multi-channel FFT (CDB)

[IMAGE alt='image' src='2d_inverse_multi-channel_fft__cdb.gif']

|  | shift? specifies whether the DC component is at the center of each channel of Multi-channel FFT {X}. The default is FALSE. |
| --- | --- |
|  | Multi-channel FFT {X} specifies frequency-domain sequences by rows or columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform inverse FFT on each row of Multi-channel FFT {X} or each column of Multi-channel FFT {X}. 0Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}.1Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
| 0 | Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}. |
| 1 | Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
|  | X returns the inverse FFT result of each channel in Multi-channel FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Inverse Multi-channel FFT (CSG)

[IMAGE alt='image' src='2d_inverse_multi-channel_fft__csg.gif']

|  | shift? specifies whether the DC component is at the center of each channel of Multi-channel FFT {X}. The default is FALSE. |
| --- | --- |
|  | Multi-channel FFT {X} specifies frequency-domain sequences by rows or columns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform inverse FFT on each row of Multi-channel FFT {X} or each column of Multi-channel FFT {X}. 0Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}.1Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
| 0 | Row-wise (default)—Each row of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each row of Multi-channel FFT {X}. |
| 1 | Column-wise—Each column of Multi-channel FFT {X} is one channel frequency-domain sequence. Specifies that this VI performs inverse FFT on each column of Multi-channel FFT {X}. |
|  | X returns the inverse FFT result of each channel in Multi-channel FFT {X}. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Inverse Multi-channel FFT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_kronecker_product.html language=enus -->
## TOPIC 00067: Kronecker Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_kronecker_product.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_kronecker_product.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Kronecker Product VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the Kronecker product of the input matrices **A** and **B**.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Kronecker Product (DBL)

[IMAGE alt='image' src='kronecker_product__dbl.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Kronecker Product returns the computed Kronecker product of matrices A and B. The number of rows in Kronecker Product is the product of the number of rows in A and B. The number of columns in Kronecker Product is the product of the number of columns in A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Kronecker Product (SGL)

[IMAGE alt='image' src='kronecker_product__sgl.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Kronecker Product returns the computed Kronecker product of matrices A and B. The number of rows in Kronecker Product is the product of the number of rows in A and B. The number of columns in Kronecker Product is the product of the number of columns in A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Kronecker Product (CDB)

[IMAGE alt='image' src='kronecker_product__cdb.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Kronecker Product returns the computed Kronecker product of matrices A and B. The number of rows in Kronecker Product is the product of the number of rows in A and B. The number of columns in Kronecker Product is the product of the number of columns in A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Kronecker Product (CSG)

[IMAGE alt='image' src='kronecker_product__csg.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Kronecker Product returns the computed Kronecker product of matrices A and B. The number of rows in Kronecker Product is the product of the number of rows in A and B. The number of columns in Kronecker Product is the product of the number of columns in A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Kronecker Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/kroneck.html) section in the [Kronecker Product](/csh?topicname=gmath/kroneck.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_linalg_axb.html language=enus -->
## TOPIC 00068: A x B VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_linalg_axb.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_linalg_axb.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### A x B VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the product of two matrices or a matrix and a vector. The data types you wire to the **A** and **B** inputs determine the polymorphic instance to use.

[Details](#details)

#### A x B (DBL)

[IMAGE alt='image' src='a_x_b__dbl.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the product of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x B (SGL)

[IMAGE alt='image' src='a_x_b__sgl.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the product of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x B (CDB)

[IMAGE alt='image' src='a_x_b__cdb.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the product of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x B (CSG)

[IMAGE alt='image' src='a_x_b__csg.gif']

|  | A specifies the first matrix. |
| --- | --- |
|  | B specifies the second matrix. The number of rows in B must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x B returns the product of A and B. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x Vector (DBL)

[IMAGE alt='image' src='a_x_vector__dbl.gif']

|  | A specifies a matrix. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the product of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x Vector (SGL)

[IMAGE alt='image' src='a_x_vector__sgl.gif']

|  | A specifies a matrix. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the product of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x Vector (CDB)

[IMAGE alt='image' src='a_x_vector__cdb.gif']

|  | A specifies a matrix. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the product of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x Vector (CSG)

[IMAGE alt='image' src='a_x_vector__csg.gif']

|  | A specifies a matrix. |
| --- | --- |
|  | Vector specifies a vector. The number of elements in Vector must match the number of columns in A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | A x Vector returns the product of A and Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x A (DBL)

[IMAGE alt='image' src='vector_x_a__dbl.gif']

|  | Vector specifies a vector. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the product of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x A (SGL)

[IMAGE alt='image' src='vector_x_a__sgl.gif']

|  | Vector specifies a vector. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the product of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x A (CDB)

[IMAGE alt='image' src='vector_x_a__cdb.gif']

|  | Vector specifies a vector. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the product of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector x A (CSG)

[IMAGE alt='image' src='vector_x_a__csg.gif']

|  | Vector specifies a vector. |
| --- | --- |
|  | A specifies a matrix. The number of rows in A must match the number of elements in Vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector x A returns the product of Vector and A. |
|  | error out contains error information. This output provides standard error out functionality. |

#### A x B Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/a_x_b.html) section in the [A x B](/csh?topicname=gmath/a_x_b.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_linalg_create_special_matrix.html language=enus -->
## TOPIC 00069: Create Special Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_linalg_create_special_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_linalg_create_special_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Create Special Matrix VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Generates a special matrix based on **matrix type**.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

Let *n* represent matrix size, X represent **Input Vector1**, *nx* represent the size of X, Y represent **Input Vector2**, *ny* represent the size of Y, B represent the output **Special Matrix**, and *b*<sub>*i*</sub>,<sub>*j*</sub> represent the element of B in the *i*th row and *j*th column.

[Details](#details)

#### Create Special Matrix (DBL)

[IMAGE alt='image' src='create_special_matrix__dbl.gif']

|  | Input Vector2 specifies the Y variable to construct a special matrix. |
| --- | --- |
|  | matrix type specifies the type of special matrix to generate. 0Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2.1Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2.2Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X.3Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2.4Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2.5Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
| 0 | Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2. |
| 1 | Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2. |
| 2 | Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X. |
| 3 | Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2. |
| 4 | Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2. |
| 5 | Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
|  | matrix size specifies the dimension size of Special Matrix. The default is 1. This VI ignores matrix size unless the value of matrix type is Identity. |
|  | Input Vector1 specifies the X variable to construct a special matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Special Matrix returns the generated matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (SGL)

[IMAGE alt='image' src='create_special_matrix__sgl.gif']

|  | Input Vector2 specifies the Y variable to construct a special matrix. |
| --- | --- |
|  | matrix type specifies the type of special matrix to generate. 0Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2.1Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2.2Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X.3Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2.4Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2.5Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
| 0 | Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2. |
| 1 | Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2. |
| 2 | Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X. |
| 3 | Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2. |
| 4 | Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2. |
| 5 | Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
|  | matrix size specifies the dimension size of Special Matrix. The default is 1. This VI ignores matrix size unless the value of matrix type is Identity. |
|  | Input Vector1 specifies the X variable to construct a special matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Special Matrix returns the generated matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (CDB)

[IMAGE alt='image' src='create_special_matrix__cdb.gif']

|  | Input Vector2 specifies the Y variable to construct a special matrix. |
| --- | --- |
|  | matrix type specifies the type of special matrix to generate. 0Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2.1Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2.2Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X.3Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2.4Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2.5Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
| 0 | Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2. |
| 1 | Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2. |
| 2 | Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X. |
| 3 | Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2. |
| 4 | Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2. |
| 5 | Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
|  | matrix size specifies the dimension size of Special Matrix. The default is 1. This VI ignores matrix size unless the value of matrix type is Identity. |
|  | Input Vector1 specifies the X variable to construct a special matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Special Matrix returns the generated matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix (CSG)

[IMAGE alt='image' src='create_special_matrix__csg.gif']

|  | Input Vector2 specifies the Y variable to construct a special matrix. |
| --- | --- |
|  | matrix type specifies the type of special matrix to generate. 0Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2.1Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2.2Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X.3Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2.4Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2.5Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
| 0 | Identity (default)—Generates an n-by-n identity matrix. This VI ignores Input Vector1 and Input Vector2. |
| 1 | Diagonal—Generates an nx-by-nx diagonal matrix whose diagonal elements are the elements of X. This VI ignores Input Vector2. |
| 2 | Toeplitz—Generates an nx-by-ny Toeplitz matrix, which has X as its first column and Y as its first row. If the first element of X and Y are different, this VI uses the first element of X. |
| 3 | Vandermonde—Generates an nx-by-nx Vandermonde matrix whose columns are powers of the elements of X. The elements of a Vandermonde matrix are:bi,j = xinx – j –1 where i, j=0…nx–1. This VI ignores Input Vector2. |
| 4 | Companion—Generates an (nx-1)-by-(nx-1) companion matrix. If vector X is a vector of a polynomial coefficient, the first element of X is the coefficient of the highest order, the last element of X is the constant term in the polynomial, the corresponding companion matrix is constructed as follows: the first row is and the subdiagonal elements of B are 1.The eigenvalues of a companion matrix contain the roots of the corresponding polynomial. This VI ignores Input Vector2. |
| 5 | Hankel—Generates an nx-by-ny Hankel matrix, where X is the first column and Y is the last row of the matrix. If the first element of Y and the last element of X are different, this VI uses the last element of X. |
|  | matrix size specifies the dimension size of Special Matrix. The default is 1. This VI ignores matrix size unless the value of matrix type is Identity. |
|  | Input Vector1 specifies the X variable to construct a special matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Special Matrix returns the generated matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Create Special Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_linalg_trace.html language=enus -->
## TOPIC 00070: Trace VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_linalg_trace.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_linalg_trace.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Trace VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the trace of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Trace (DBL)

[IMAGE alt='image' src='trace__dbl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets trace to NaN. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (SGL)

[IMAGE alt='image' src='trace__sgl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets trace to NaN. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (CDB)

[IMAGE alt='image' src='trace__cdb.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets trace to NaN + NaNi. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (CSG)

[IMAGE alt='image' src='trace__csg.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets trace to NaN + NaNi. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/trace.html) section in the [Trace](/csh?topicname=gmath/trace.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_linalg_transpose.html language=enus -->
## TOPIC 00071: Transpose Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_linalg_transpose.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_linalg_transpose.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Transpose Matrix VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Finds the transpose of real **Input Matrix** or the conjugate transpose of complex**Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Transpose Matrix (DBL)

[IMAGE alt='image' src='transpose_matrix__dbl.gif']

|  | Input Matrix specifies a square or rectangular matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Transpose returns the transpose of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (SGL)

[IMAGE alt='image' src='transpose_matrix__sgl.gif']

|  | Input Matrix specifies a square or rectangular matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Transpose returns the transpose of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (CDB)

[IMAGE alt='image' src='transpose_matrix__cdb.gif']

|  | Input Matrix specifies a square or rectangular matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Conjugate Transpose returns the conjugate transpose of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (CSG)

[IMAGE alt='image' src='transpose_matrix__csg.gif']

|  | Input Matrix specifies a square or rectangular matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Conjugate Transpose returns the conjugate transpose of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_linear_algebra_vis.html language=enus -->
## TOPIC 00072: Linear Algebra VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_linear_algebra_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_linear_algebra_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Linear Algebra VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Linear Algebra VIs to perform matrix-related computations and analysis.

| Palette Object | Description |
| --- | --- |
| A x B | Computes the product of two matrices or a matrix and a vector. The data types you wire to the A and B inputs determine the polymorphic instance to use. |
| Cholesky Decomposition | Computes the Cholesky decomposition of a symmetric or Hermitian positive definite matrix A. |
| Create Special Matrix | Generates a special matrix based on matrix type. |
| Determinant | Computes the determinant of Input Matrix. |
| Dot Product | Computes the dot product of X Vector and Y Vector. |
| Eigenvalues and Vectors | Finds the eigenvalues and right eigenvectors of the square Input Matrix. |
| Generalized Eigenvalues and Vectors | Computes the generalized eigenvalue and eigenvectors of a pair of matrices A and B. |
| Inverse Matrix | Finds the inverse, if it exists, of Input Matrix. |
| Kronecker Product | Computes the Kronecker product of the input matrices A and B. |
| LU Decomposition | Computes the LU decomposition of a matrix A so that PA = LU. |
| Matrix Condition Number | Computes the condition number of Input Matrix. |
| Matrix Exponential | Computes the exponential of Input Matrix. |
| Matrix Logarithm | Computes the natural logarithm of Input Matrix. |
| Matrix Norm | Computes the norm of Input Matrix. |
| Matrix Power | Computes the nth power of Input Matrix. |
| Matrix Rank | Computes the rank of Input Matrix. |
| Matrix Square Root | Computes the square root of Input Matrix. |
| Outer Product | Computes the outer product of X Vector and Y Vector. The data types you wire to the X Vector and Y Vector inputs determine the polymorphic instance to use. |
| PseudoInverse Matrix | Finds the pseudoinverse of Input Matrix. |
| QR Decomposition | Computes the QR decomposition of a matrix A. |
| QZ Decomposition | Computes the QZ decomposition of a pair of matrices A and B. |
| Schur Decomposition | Computes the Schur decomposition of the Input Matrix. |
| Solve Linear Equations | Finds the solution to a linear system AX = Y. |
| SVD Decomposition | Computes the singular value decomposition (SVD) of a matrix A. |
| Trace | Computes the trace of Input Matrix. |
| Transpose Matrix | Finds the transpose of real Input Matrix or the conjugate transpose of complex Input Matrix. |
| Vector Norm | Computes the norm of Input Vector. |

| Subpalette | Description |
| --- | --- |
| Basic Linear Algebra Subroutines VIs | Use the Basic Linear Algebra Subroutines VIs to perform basic scalar-vector, vector-vector, matrix-vector, and matrix-matrix operations. |
| Sparse Linear Algebra VIs | Use the Sparse Linear Algebra VIs to perform linear algebra computations and analysis on sparse matrices. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_lu_decomp.html language=enus -->
## TOPIC 00073: LU Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_lu_decomp.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_lu_decomp.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### LU Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the LU decomposition of a matrix **A** so that **PA** = **LU**.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### LU Decomposition (DBL)

[IMAGE alt='image' src='lu_decomposition__dbl.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | L returns the decomposed m × min(m, n) lower triangular matrix with ones as the diagonal elements. |
|  | U returns the decomposed min(m, n) × n upper triangular matrix. |
|  | P returns the decomposed m × m permutation matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### LU Decomposition (SGL)

[IMAGE alt='image' src='lu_decomposition__sgl.gif']

|  | A is an m × n matrix with m rows and n columns. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | L returns the decomposed m × min(m, n) lower triangular matrix with ones as the diagonal elements. |
|  | U returns the decomposed min(m, n) × n upper triangular matrix. |
|  | P returns the decomposed m × m permutation matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### LU Decomposition (CDB)

[IMAGE alt='image' src='lu_decomposition__cdb.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | L returns the decomposed m × min(m, n) lower triangular matrix with ones as the diagonal elements. |
|  | U returns the decomposed min(m, n) × n upper triangular matrix. |
|  | P returns the decomposed m × m permutation matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### LU Decomposition (CSG)

[IMAGE alt='image' src='lu_decomposition__csg.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | L returns the decomposed m × min(m, n) lower triangular matrix with ones as the diagonal elements. |
|  | U returns the decomposed min(m, n) × n upper triangular matrix. |
|  | P returns the decomposed m × m permutation matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### LU Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instance is an exception: LU Decomposition (DBL) |

Refer to the [Details](/csh?topicname=gmath/lu_factorization.html) section in the [LU Factorization](/csh?topicname=gmath/lu_factorization.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_condition_num.html language=enus -->
## TOPIC 00074: Matrix Condition Number VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_condition_num.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_condition_num.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Condition Number VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the condition number of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Condition Number (DBL)

[IMAGE alt='image' src='matrix_condition_number__dbl.gif']

|  | Input Matrix specifies a square matrix. If norm type is 2-norm, Input Matrix can be a rectangular matrix. If Input Matrix is empty, this VI sets condition number to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm this VI uses to compute the condition number. Refer to the Matrix Norm VI for a definition of a matrix norm. 02-norm (default)11-norm2F-norm3Inf-norm |
| 0 | 2-norm (default) |
| 1 | 1-norm |
| 2 | F-norm |
| 3 | Inf-norm |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | condition number returns the condition number of Input Matrix for the specified norm type. If norm type is 2-norm, the condition number is the ratio of the largest singular value of Input Matrix to the smallest singular value of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Condition Number (SGL)

[IMAGE alt='image' src='matrix_condition_number__sgl.gif']

|  | Input Matrix specifies a square matrix. If norm type is 2-norm, Input Matrix can be a rectangular matrix. If Input Matrix is empty, this VI sets condition number to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm this VI uses to compute the condition number. Refer to the Matrix Norm VI for a definition of a matrix norm. 02-norm (default)11-norm2F-norm3Inf-norm |
| 0 | 2-norm (default) |
| 1 | 1-norm |
| 2 | F-norm |
| 3 | Inf-norm |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | condition number returns the condition number of Input Matrix for the specified norm type. If norm type is 2-norm, the condition number is the ratio of the largest singular value of Input Matrix to the smallest singular value of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Condition Number (CDB)

[IMAGE alt='image' src='matrix_condition_number__cdb.gif']

|  | Input Matrix specifies a square matrix. If norm type is 2-norm, Input Matrix can be a rectangular matrix. If Input Matrix is empty, this VI sets condition number to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm this VI uses to compute the condition number. Let A represent the Input Matrix, the norm of A is represented by \|\|A\|\|p, where p is the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of A.11-norm—\|\|A\|\|1 is the largest absolute column of A.2F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A.3inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A. |
| 3 | inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | condition number returns the condition number of Input Matrix for the specified norm type. If norm type is 2-norm, the condition number is the ratio of the largest singular value of Input Matrix to the smallest singular value of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Condition Number (CSG)

[IMAGE alt='image' src='matrix_condition_number__csg.gif']

|  | Input Matrix specifies a square matrix. If norm type is 2-norm, Input Matrix can be a rectangular matrix. If Input Matrix is empty, this VI sets condition number to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm this VI uses to compute the condition number. Let A represent the Input Matrix, the norm of A is represented by \|\|A\|\|p, where p is the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of A.11-norm—\|\|A\|\|1 is the largest absolute column of A.2F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A.3inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A. |
| 3 | inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | condition number returns the condition number of Input Matrix for the specified norm type. If norm type is 2-norm, the condition number is the ratio of the largest singular value of Input Matrix to the smallest singular value of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Condition Number Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following cases are exceptions: Matrix Condition Number (DBL) when norm type is 1–norm, F–norm or Inf–norm |

Refer to the [Details](/csh?topicname=gmath/matrix_condition_number.html) section in the [Matrix Condition Number](/csh?topicname=gmath/matrix_condition_number.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_exponential.html language=enus -->
## TOPIC 00075: Matrix Exponential VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_exponential.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_exponential.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Exponential VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the exponential of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Exponential (DBL)

[IMAGE alt='image' src='matrix_exponential__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Exponential to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Exponential returns the exponential of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Exponential (SGL)

[IMAGE alt='image' src='matrix_exponential__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Exponential to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Exponential returns the exponential of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Exponential (CDB)

[IMAGE alt='image' src='matrix_exponential__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Exponential to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Exponential returns the exponential of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Exponential (CSG)

[IMAGE alt='image' src='matrix_exponential__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Exponential to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Exponential returns the exponential of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Exponential Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instance is an exception: Matrix Exponential (DBL) |

Refer to the [Details](/csh?topicname=gmath/matrix_exp.html) section in the [Matrix Exp](/csh?topicname=gmath/matrix_exp.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_logarithm.html language=enus -->
## TOPIC 00076: Matrix Logarithm VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_logarithm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_logarithm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Logarithm VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the natural logarithm of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Logarithm (DBL)

[IMAGE alt='image' src='matrix_logarithm__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Logarithm to an empty matrix. |
| --- | --- |
|  | logarithm option specifies the type of logarithm to return. 0General (default)—Specifies that Input Matrix is regarded as a complex matrix.1Real—Specifies to return an exact real logarithm when Input Matrix is a non-singular normal matrix and each of the negative eigenvalues occurs an even number of times. When Input Matrix is not normal or one of its eigenvalues occurs an odd number of times, this VI returns Matrix Logarithm as if logarithm option were General. |
| 0 | General (default)—Specifies that Input Matrix is regarded as a complex matrix. |
| 1 | Real—Specifies to return an exact real logarithm when Input Matrix is a non-singular normal matrix and each of the negative eigenvalues occurs an even number of times. When Input Matrix is not normal or one of its eigenvalues occurs an odd number of times, this VI returns Matrix Logarithm as if logarithm option were General. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Logarithm returns the natural logarithm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Logarithm (SGL)

[IMAGE alt='image' src='matrix_logarithm__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Logarithm to an empty matrix. |
| --- | --- |
|  | logarithm option specifies the type of logarithm to return. 0General (default)—Specifies that Input Matrix is regarded as a complex matrix.1Real—Specifies to return an exact real logarithm when Input Matrix is a non-singular normal matrix and each of the negative eigenvalues occurs an even number of times. When Input Matrix is not normal or one of its eigenvalues occurs an odd number of times, this VI returns Matrix Logarithm as if logarithm option were General. |
| 0 | General (default)—Specifies that Input Matrix is regarded as a complex matrix. |
| 1 | Real—Specifies to return an exact real logarithm when Input Matrix is a non-singular normal matrix and each of the negative eigenvalues occurs an even number of times. When Input Matrix is not normal or one of its eigenvalues occurs an odd number of times, this VI returns Matrix Logarithm as if logarithm option were General. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Logarithm returns the natural logarithm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Logarithm (CDB)

[IMAGE alt='image' src='matrix_logarithm__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Logarithm to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Logarithm returns the natural logarithm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Logarithm (CSG)

[IMAGE alt='image' src='matrix_logarithm__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Logarithm to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Logarithm returns the natural logarithm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Logarithm Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/matrix_logarithm.html) section in the [Matrix Logarithm](/csh?topicname=gmath/matrix_logarithm.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_norm.html language=enus -->
## TOPIC 00077: Matrix Norm VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_norm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_norm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Norm VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the norm of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Norm (DBL)

[IMAGE alt='image' src='matrix_norm__dbl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm to compute. Let A represent the Input Matrix, \|\|A\|\|p represents the norm of A, where p can be the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of the A.11-norm—\|\|A\|\|1 is the largest absolute column sum of A.2F-norm—\|\|A\|\|F is equal to where tr(ATA) is the trace of matrix ATA and AT is the transpose of A.3Inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of the A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column sum of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(ATA) is the trace of matrix ATA and AT is the transpose of A. |
| 3 | Inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Norm (SGL)

[IMAGE alt='image' src='matrix_norm__sgl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm to compute. Let A represent the Input Matrix, \|\|A\|\|p represents the norm of A, where p can be the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of the A.11-norm—\|\|A\|\|1 is the largest absolute column sum of A.2F-norm—\|\|A\|\|F is equal to where tr(ATA) is the trace of matrix ATA and AT is the transpose of A.3Inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of the A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column sum of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(ATA) is the trace of matrix ATA and AT is the transpose of A. |
| 3 | Inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Norm (CDB)

[IMAGE alt='image' src='matrix_norm__cdb.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm to compute. Let A represent the Input Matrix, the norm of A is represented by \|\|A\|\|p, where p is the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of A.11-norm—\|\|A\|\|1 is the largest absolute column of A.2F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A.3inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A. |
| 3 | inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Norm (CSG)

[IMAGE alt='image' src='matrix_norm__csg.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of matrix norm to compute. Let A represent the Input Matrix, the norm of A is represented by \|\|A\|\|p, where p is the different types of norms that this VI computes. 02-norm (default)—\|\|A\|\|2 is the largest singular value of A.11-norm—\|\|A\|\|1 is the largest absolute column of A.2F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A.3inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
| 0 | 2-norm (default)—\|\|A\|\|2 is the largest singular value of A. |
| 1 | 1-norm—\|\|A\|\|1 is the largest absolute column of A. |
| 2 | F-norm—\|\|A\|\|F is equal to where tr(AHA) is the trace of matrix AHA and AH is the conjugate transpose of A. |
| 3 | inf-norm—\|\|A\|\| is the largest absolute row sum of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Norm Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_power.html language=enus -->
## TOPIC 00078: Matrix Power VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_power.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_power.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Power VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the *n*<sup>th</sup> power of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Power (DBL)

[IMAGE alt='image' src='matrix_power__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Power to an empty matrix. |
| --- | --- |
|  | n specifies the order of the power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Power returns the nth of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Power (SGL)

[IMAGE alt='image' src='matrix_power__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Power to an empty matrix. |
| --- | --- |
|  | n specifies the order of the power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Power returns the nth of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Power (CDB)

[IMAGE alt='image' src='matrix_power__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Power to an empty matrix. |
| --- | --- |
|  | n specifies the order of the power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Power returns the nth of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Power (CSG)

[IMAGE alt='image' src='matrix_power__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Power to an empty matrix. |
| --- | --- |
|  | n specifies the order of the power. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Power returns the nth of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Power Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_rank.html language=enus -->
## TOPIC 00079: Matrix Rank VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_rank.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_rank.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Rank VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the rank of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Rank (DBL)

[IMAGE alt='image' src='matrix_rank__dbl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets rank to -1. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a double-precision machine epsilon, as shown in the following relationship. = 2–52 = 2.22e – 16 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rank returns the number of singular values in the Input Matrix that are larger than the tolerance. The rank represents the maximum number of independent rows or columns in the Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Rank (SGL)

[IMAGE alt='image' src='matrix_rank__sgl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets rank to -1. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a single-precision machine epsilon, as shown in the following relationship. = 2–23 = 1.19e – 7 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rank returns the number of singular values in the Input Matrix that are larger than the tolerance. The rank represents the maximum number of independent rows or columns in the Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Rank (CDB)

[IMAGE alt='image' src='matrix_rank__cdb.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets rank to -1. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a double-precision machine epsilon, as shown in the following relationship. = 2–52 = 2.22e – 16 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rank returns the number of singular values in the Input Matrix that are larger than the tolerance. The rank represents the maximum number of independent rows or columns in the Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Rank (CSG)

[IMAGE alt='image' src='matrix_rank__csg.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is empty, this VI sets rank to -1. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a single-precision machine epsilon, as shown in the following relationship. = 2–23 = 1.19e – 7 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | rank returns the number of singular values in the Input Matrix that are larger than the tolerance. The rank represents the maximum number of independent rows or columns in the Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Rank Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_sq_rt.html language=enus -->
## TOPIC 00080: Matrix Square Root VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_sq_rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_sq_rt.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix Square Root VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the square root of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Matrix Square Root (DBL)

[IMAGE alt='image' src='matrix_square_root__dbl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Square Root to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Square Root returns the square root of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Square Root (SGL)

[IMAGE alt='image' src='matrix_square_root__sgl.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Square Root to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Square Root returns the square root of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Square Root (CDB)

[IMAGE alt='image' src='matrix_square_root__cdb.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Square Root to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Square Root returns the square root of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Square Root (CSG)

[IMAGE alt='image' src='matrix_square_root__csg.gif']

|  | Input Matrix specifies a square matrix. If Input Matrix is empty, this VI sets Matrix Square Root to an empty matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Square Root returns the square root of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Matrix Square Root Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_matrix_vis.html language=enus -->
## TOPIC 00081: Matrix VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_matrix_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_matrix_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Matrix VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Matrix VIs to manipulate the elements, diagonals, and submatrices of a sparse matrix.

| Palette Object | Description |
| --- | --- |
| Build Matrix | Builds four sparse matrices by column and then by row. |
| Concatenate Matrix | Concatenates two sparse matrices by row, column, or diagonal. |
| Create Matrix from Storage Format | Creates a sparse matrix from storage format. |
| Dense to Sparse | Converts a dense matrix to a sparse matrix that contains only nonzero elements. |
| Get Matrix Size | Returns the number of rows and columns in a sparse matrix. |
| Get Matrix Storage Format | Gets the storage format of a sparse matrix. |
| Get Matrix Subset | Gets a subset from a sparse matrix. |
| Get Number of Nonzeros | Returns the number of nonzeros and the maximum number of nonzeros in a sparse matrix. |
| Initialize Matrix | Initializes a zero sparse matrix with the specified number of row and columns. |
| Non-Conjugate Transpose Matrix | Computes the non-conjugate transpose of a sparse matrix. |
| Reorder Elements | Reorders elements in a sparse matrix according to their row and column indices. Reordering elements in a sparse matrix usually speeds up sparse matrix operations. |
| Set Matrix Size | Sets the number of rows and columns in a sparse matrix. |
| Set Matrix Subset | Sets a subset in a sparse matrix. |
| Set Max Number of Nonzeros | Sets the maximum number of nonzeros in a sparse matrix. |
| Sparse to Dense | Converts a sparse matrix to a dense matrix that contains zero elements explicitly. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_multichannel_fft.html language=enus -->
## TOPIC 00082: Multi-channel FFT VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_multichannel_fft.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_multichannel_fft.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multi-channel FFT VI

**Owning Palette:** [Transforms VIs](../lvmasmtref/masm_transforms_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the fast Fourier transform (FFT) of each channel signal of the input matrix **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### 2D Multi-channel FFT (DBL)

[IMAGE alt='image' src='2d_multi-channel_fft__dbl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of each channel FFT result. The default is FALSE. |
| --- | --- |
|  | X specifies the multi-channel input signal. |
|  | FFT size specifies the length of the FFT you want to perform on each channel signal. If FFT size is greater than the length of each channel signal in X, this VI adds zeros to the each channel signal in X to match the size of FFT size. If FFT size is less than the length of each channel signal in X, this VI uses only the first n elements of each channel signal in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI does not zero pad or truncate X. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform FFT on each row of X or each column of X. 0Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X.1Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
| 0 | Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X. |
| 1 | Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
|  | Multi-channel FFT {X} returns each channel FFT result of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Multi-channel FFT (SGL)

[IMAGE alt='image' src='2d_multi-channel_fft__sgl.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of each channel FFT result. The default is FALSE. |
| --- | --- |
|  | X specifies the multi-channel input signal. |
|  | FFT size specifies the length of the FFT you want to perform on each channel signal. If FFT size is greater than the length of each channel signal in X, this VI adds zeros to the each channel signal in X to match the size of FFT size. If FFT size is less than the length of each channel signal in X, this VI uses only the first n elements of each channel signal in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI does not zero pad or truncate X. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform FFT on each row of X or each column of X. 0Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X.1Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
| 0 | Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X. |
| 1 | Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
|  | Multi-channel FFT {X} returns each channel FFT result of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Multi-channel FFT (CDB)

[IMAGE alt='image' src='2d_multi-channel_fft__cdb.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of each channel FFT result. The default is FALSE. |
| --- | --- |
|  | X specifies the multi-channel input signal. |
|  | FFT size specifies the length of the FFT you want to perform on each channel signal. If FFT size is greater than the length of each channel signal in X, this VI adds zeros to the each channel signal in X to match the size of FFT size. If FFT size is less than the length of each channel signal in X, this VI uses only the first n elements of each channel signal in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI does not zero pad or truncate X. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform FFT on each row of X or each column of X. 0Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X.1Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
| 0 | Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X. |
| 1 | Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
|  | Multi-channel FFT {X} returns each channel FFT result of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### 2D Multi-channel FFT (CSG)

[IMAGE alt='image' src='2d_multi-channel_fft__csg.gif']

|  | shift? specifies whether this VI shifts the DC component to the center of each channel FFT result. The default is FALSE. |
| --- | --- |
|  | X specifies the multi-channel input signal. |
|  | FFT size specifies the length of the FFT you want to perform on each channel signal. If FFT size is greater than the length of each channel signal in X, this VI adds zeros to the each channel signal in X to match the size of FFT size. If FFT size is less than the length of each channel signal in X, this VI uses only the first n elements of each channel signal in X to perform the FFT, where n is the FFT size. If FFT size is less than or equal to zero, this VI does not zero pad or truncate X. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FFT direction specifies whether to perform FFT on each row of X or each column of X. 0Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X.1Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
| 0 | Row-wise (default)—Each row of X is one channel signal. Specifies that this VI performs FFT on each row of X. |
| 1 | Column-wise—Each column of X is one channel signal. Specifies that this VI performs FFT on each column of X. |
|  | Multi-channel FFT {X} returns each channel FFT result of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Multi-channel FFT Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_multiply.html language=enus -->
## TOPIC 00083: Multiply VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_multiply.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_multiply.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multiply VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the element-wise product of two sparse matrices, a sparse matrix and a dense matrix, or a sparse matrix and a scalar.

[Details](#details)

#### Multiply Sparse to Sparse (DBL)

[IMAGE alt='image' src='multiply_sparse_to_sparse__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Sparse (SGL)

[IMAGE alt='image' src='multiply_sparse_to_sparse__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Sparse (CDB)

[IMAGE alt='image' src='multiply_sparse_to_sparse__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Sparse (CSG)

[IMAGE alt='image' src='multiply_sparse_to_sparse__csg.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Scalar (DBL)

[IMAGE alt='image' src='multiply_sparse_to_scalar__dbl.gif']

|  | A specifies a sparse matrix. |
| --- | --- |
|  | b specifies a scalar. |
|  | A*b returns the product of A and b. |

#### Multiply Sparse to Scalar (SGL)

[IMAGE alt='image' src='multiply_sparse_to_scalar__sgl.gif']

|  | A specifies a sparse matrix. |
| --- | --- |
|  | b specifies a scalar. |
|  | A*b returns the product of A and b. |

#### Multiply Sparse to Scalar (CDB)

[IMAGE alt='image' src='multiply_sparse_to_scalar__cdb.gif']

|  | A specifies a sparse matrix. |
| --- | --- |
|  | b specifies a scalar. |
|  | A*b returns the product of A and b. |

#### Multiply Sparse to Scalar (CSG)

[IMAGE alt='image' src='multiply_sparse_to_scalar__csg.gif']

|  | A specifies a sparse matrix. |
| --- | --- |
|  | b specifies a scalar. |
|  | A*b returns the product of A and b. |

#### Multiply Scalar to Sparse (DBL)

[IMAGE alt='image' src='multiply_scalar_to_sparse__dbl.gif']

|  | a specifies a scalar. |
| --- | --- |
|  | B specifies a sparse matrix. |
|  | a*B returns the product of a and B. |

#### Multiply Scalar to Sparse (SGL)

[IMAGE alt='image' src='multiply_scalar_to_sparse__sgl.gif']

|  | a specifies a scalar. |
| --- | --- |
|  | B specifies a sparse matrix. |
|  | a*B returns the product of a and B. |

#### Multiply Scalar to Sparse (CDB)

[IMAGE alt='image' src='multiply_scalar_to_sparse__cdb.gif']

|  | a specifies a scalar. |
| --- | --- |
|  | B specifies a sparse matrix. |
|  | a*B returns the product of a and B. |

#### Multiply Scalar to Sparse (CSG)

[IMAGE alt='image' src='multiply_scalar_to_sparse__csg.gif']

|  | a specifies a scalar. |
| --- | --- |
|  | B specifies a sparse matrix. |
|  | a*B returns the product of a and B. |

#### Multiply Sparse to Dense (DBL)

[IMAGE alt='image' src='multiply_sparse_to_dense__dbl.gif']

|  | A specifies a sparse matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a dense matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Dense (SGL)

[IMAGE alt='image' src='multiply_sparse_to_dense__sgl.gif']

|  | A specifies a sparse matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a dense matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Dense (CDB)

[IMAGE alt='image' src='multiply_sparse_to_dense__cdb.gif']

|  | A specifies a sparse matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a dense matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Sparse to Dense (CSG)

[IMAGE alt='image' src='multiply_sparse_to_dense__csg.gif']

|  | A specifies a sparse matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a dense matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Dense to Sparse (DBL)

[IMAGE alt='image' src='multiply_dense_to_sparse__dbl.gif']

|  | A specifies a dense matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies a sparse matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Dense to Sparse (SGL)

[IMAGE alt='image' src='multiply_dense_to_sparse__sgl.gif']

|  | A specifies a dense matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a sparse matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Dense to Sparse (CDB)

[IMAGE alt='image' src='multiply_dense_to_sparse__cdb.gif']

|  | A specifies a dense matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a sparse matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Dense to Sparse (CSG)

[IMAGE alt='image' src='multiply_dense_to_sparse__csg.gif']

|  | A specifies a dense matrix. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a sparse matrix. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A*B returns the element-wise product of A and B. |

#### Multiply Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: Multiply Sparse to Sparse (DBL) Multiply Sparse to Sparse (SGL) Multiply Sparse to Sparse (CDB) Multiply Sparse to Sparse (CSG) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_negate.html language=enus -->
## TOPIC 00084: Negate VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_negate.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_negate.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Negate VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Negates elements in a sparse matrix.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Negate Sparse Matrix (DBL)

[IMAGE alt='image' src='negate_sparse_matrix__dbl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | -A returns a sparse matrix whose elements are the negative elements in A. |

#### Negate Sparse Matrix (SGL)

[IMAGE alt='image' src='negate_sparse_matrix__sgl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | -A returns a sparse matrix whose elements are the negative elements in A. |

#### Negate Sparse Matrix (CDB)

[IMAGE alt='image' src='negate_sparse_matrix__cdb.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | -A returns a sparse matrix whose elements are the negative elements in A. |

#### Negate Sparse Matrix (CSG)

[IMAGE alt='image' src='negate_sparse_matrix__csg.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | -A returns a sparse matrix whose elements are the negative elements in A. |

#### Negate Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_nonconj_transp_sparse_matrix.html language=enus -->
## TOPIC 00085: Non-Conjugate Transpose Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_nonconj_transp_sparse_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_nonconj_transp_sparse_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Non-Conjugate Transpose Matrix VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the non-conjugate transpose of a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Non-Conj Transpose Sparse Matrix (DBL)

[IMAGE alt='image' src='non-conj_transpose_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Transposed Sparse Matrix returns the non-conjugate transpose of Sparse Matrix. |

#### Non-Conj Transpose Sparse Matrix (SGL)

[IMAGE alt='image' src='non-conj_transpose_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Transposed Sparse Matrix returns the non-conjugate transpose of Sparse Matrix. |

#### Non-Conj Transpose Sparse Matrix (CDB)

[IMAGE alt='image' src='non-conj_transpose_sparse_matrix__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Transposed Sparse Matrix returns the non-conjugate transpose of Sparse Matrix. |

#### Non-Conj Transpose Sparse Matrix (CSG)

[IMAGE alt='image' src='non-conj_transpose_sparse_matrix__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | Transposed Sparse Matrix returns the non-conjugate transpose of Sparse Matrix. |

#### Non-Conjugate Transpose Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_not_equal.html language=enus -->
## TOPIC 00086: Not Equal VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_not_equal.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_not_equal.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Not Equal VI

**Owning Palette:** [Comparison VIs](../lvmasmtref/masm_comparison_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Returns TRUE if two sparse matrices are not equal. Otherwise, this VI returns FALSE.

Two matrices are not equal if either they have different sizes or one of corresponding elements have different values.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Not Equal Sparse Matrix (DBL)

[IMAGE alt='image' src='not_equal_sparse_matrix__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A != B? returns TRUE if A is not equal to B. Otherwise, returns FALSE. |

#### Not Equal Sparse Matrix (SGL)

[IMAGE alt='image' src='not_equal_sparse_matrix__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A != B? returns TRUE if A is not equal to B. Otherwise, returns FALSE. |

#### Not Equal Sparse Matrix (CDB)

[IMAGE alt='image' src='not_equal_sparse_matrix__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A != B? returns TRUE if A is not equal to B. Otherwise, returns FALSE. |

#### Not Equal Sparse Matrix (CSG)

[IMAGE alt='image' src='not_equal_sparse_matrix__csg.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A != B? returns TRUE if A is not equal to B. Otherwise, returns FALSE. |

#### Not Equal Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_numeric_vis.html language=enus -->
## TOPIC 00087: Numeric VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_numeric_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_numeric_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Numeric VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Numeric VIs to create and perform arithmetic and complex mathematical operations on sparse matrices and to convert sparse matrices from one data type to another.

| Palette Object | Description |
| --- | --- |
| Absolute Value | Computes the absolute values of elements in a sparse matrix. |
| Add | Computes the element-wise sum of two sparse matrices. |
| Multiply | Computes the element-wise product of two sparse matrices, a sparse matrix and a dense matrix, or a sparse matrix and a scalar. |
| Negate | Negates elements in a sparse matrix. |
| Square | Computes the square of elements in a sparse matrix. |
| Subtract | Computes the element-wise difference between two sparse matrices. |

| Subpalette | Description |
| --- | --- |
| Complex VIs | Use the Complex VIs to create a complex sparse matrix as its real and imaginary components from two real sparse matrices and to break the real and imaginary components of a complex sparse matrix into two real sparse matrices. |
| Conversion VIs | Use the Conversion VIs to convert sparse matrix data types. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_outer_product.html language=enus -->
## TOPIC 00088: Outer Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_outer_product.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_outer_product.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Outer Product VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the outer product of **X Vector** and **Y Vector**. The data types you wire to the **X Vector** and **Y Vector** inputs determine the polymorphic instance to use.

Wire data to the **X Vector** and **Y Vector** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Outer Product (DBL)

[IMAGE alt='image' src='outer_product__dbl.gif']

|  | X Vector specifies the first input vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Outer Product returns the outer product of X Vector and Y Vector. If either X Vector or Y Vector is empty, Outer Product returns an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Outer Product (SGL)

[IMAGE alt='image' src='outer_product__sgl.gif']

|  | X Vector specifies the first input vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Outer Product returns the outer product of X Vector and Y Vector. If either X Vector or Y Vector is empty, Outer Product returns an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Outer Product (CDB)

[IMAGE alt='image' src='outer_product__cdb.gif']

|  | X Vector specifies the first input vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Outer Product returns the outer product of X Vector and Y Vector. If either X Vector or Y Vector is empty, Outer Product returns an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Outer Product (CSG)

[IMAGE alt='image' src='outer_product__csg.gif']

|  | X Vector specifies the first input vector. |
| --- | --- |
|  | Y Vector specifies the second input vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Outer Product returns the outer product of X Vector and Y Vector. If either X Vector or Y Vector is empty, Outer Product returns an empty matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Outer Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/outer_product.html) section in the [Outer Product](/csh?topicname=gmath/outer_product.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pardiso_adv_clean_up.html language=enus -->
## TOPIC 00089: PARDISO Advanced Cleaning Up VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pardiso_adv_clean_up.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pardiso_adv_clean_up.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PARDISO Advanced Cleaning Up VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Cleans up the specified PARDISO session. You must clean up the session when you no longer use it.

[Details](#details)

#### PARDISO Advanced Cleaning Up (DBL)

[IMAGE alt='image' src='pardiso_advanced_cleaning_up__dbl.gif']

|  | solver ID specifies the identification number associated with the PARDISO session to clean up. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Cleaning Up (SGL)

[IMAGE alt='image' src='pardiso_advanced_cleaning_up__sgl.gif']

|  | solver ID specifies the identification number associated with the PARDISO session to clean up. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Cleaning Up (CDB)

[IMAGE alt='image' src='pardiso_advanced_cleaning_up__cdb.gif']

|  | solver ID specifies the identification number associated with the PARDISO session to clean up. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Cleaning Up (CSG)

[IMAGE alt='image' src='pardiso_advanced_cleaning_up__csg.gif']

|  | solver ID specifies the identification number associated with the PARDISO session to clean up. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Cleaning Up Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pardiso_adv_factorization.html language=enus -->
## TOPIC 00090: PARDISO Advanced Factorization VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pardiso_adv_factorization.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pardiso_adv_factorization.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PARDISO Advanced Factorization VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Performs numerical factorization on the specified PARDISO session.

You can perform numerical factorization either on the sparse matrix specified in [PARDISO Advanced Initialization](../lvmasmtref/masm_pardiso_adv_init.html) VI or on a sparse matrix which has identical size and sparsity pattern. You must initialize the PARDISO session using the PARDISO Advanced Initialization VI before performing numerical factorization.

[Details](#details)

#### PARDISO Advanced Factorization (DBL)

[IMAGE alt='image' src='pardiso_advanced_factorization__dbl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Input Matrix specifies a square sparse matrix to perform numerical factorization. If Input Matrix is not wired, LabVIEW performs numerical factorization on the sparse matrix specified in PARDISO Advanced Initialization VI. If Input Matrix is wired, LabVIEW performs numerical factorization on this sparse matrix using the analysis result from PARDISO Advanced Initialization VI. Input Matrix must have the same size and sparsity pattern as the sparse matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Factorization (SGL)

[IMAGE alt='image' src='pardiso_advanced_factorization__sgl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Input Matrix specifies a square sparse matrix to perform numerical factorization. If Input Matrix is not wired, LabVIEW performs numerical factorization on the sparse matrix specified in PARDISO Advanced Initialization VI. If Input Matrix is wired, LabVIEW performs numerical factorization on this sparse matrix using the analysis result from PARDISO Advanced Initialization VI. Input Matrix must have the same size and sparsity pattern as the sparse matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Factorization (CDB)

[IMAGE alt='image' src='pardiso_advanced_factorization__cdb.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Input Matrix specifies a square sparse matrix to perform numerical factorization. If Input Matrix is not wired, LabVIEW performs numerical factorization on the sparse matrix specified in PARDISO Advanced Initialization VI. If Input Matrix is wired, LabVIEW performs numerical factorization on this sparse matrix using the analysis result from PARDISO Advanced Initialization VI. Input Matrix must have the same size and sparsity pattern as the sparse matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Factorization (CSG)

[IMAGE alt='image' src='pardiso_advanced_factorization__csg.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Input Matrix specifies a square sparse matrix to perform numerical factorization. If Input Matrix is not wired, LabVIEW performs numerical factorization on the sparse matrix specified in PARDISO Advanced Initialization VI. If Input Matrix is wired, LabVIEW performs numerical factorization on this sparse matrix using the analysis result from PARDISO Advanced Initialization VI. Input Matrix must have the same size and sparsity pattern as the sparse matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Factorization Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pardiso_adv_init.html language=enus -->
## TOPIC 00091: PARDISO Advanced Initialization VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pardiso_adv_init.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pardiso_adv_init.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PARDISO Advanced Initialization VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Initializes a PARDISO session, attaches a sparse matrix to the initialized session, and analyzes and performs symbolic factorization on the sparse matrix. The [PARDISO Advanced Factorization](../lvmasmtref/masm_pardiso_adv_factorization.html) VI uses the analysis result for numerical factorization.

[Details](#details)

#### PARDISO Advanced Initialization (DBL)

[IMAGE alt='image' src='pardiso_advanced_initialization__dbl.gif']

|  | Input Matrix specifies a square sparse matrix to analyze and perform symbolic factorization. |
| --- | --- |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | solver ID returns the identification number associated with the PARDISO session this VI initializes. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Initialization (SGL)

[IMAGE alt='image' src='pardiso_advanced_initialization__sgl.gif']

|  | Input Matrix specifies a square sparse matrix to analyze and perform symbolic factorization. |
| --- | --- |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | solver ID returns the identification number associated with the PARDISO session this VI initializes. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Initialization (CDB)

[IMAGE alt='image' src='pardiso_advanced_initialization__cdb.gif']

|  | Input Matrix specifies a square sparse matrix to analyze and perform symbolic factorization. |
| --- | --- |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | solver ID returns the identification number associated with the PARDISO session this VI initializes. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Initialization (CSG)

[IMAGE alt='image' src='pardiso_advanced_initialization__csg.gif']

|  | Input Matrix specifies a square sparse matrix to analyze and perform symbolic factorization. |
| --- | --- |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | solver ID returns the identification number associated with the PARDISO session this VI initializes. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Initialization Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pardiso_adv_solver.html language=enus -->
## TOPIC 00092: PARDISO Advanced Solver VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pardiso_adv_solver.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pardiso_adv_solver.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PARDISO Advanced Solver VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Solves a sparse linear system *A**X* = *Y* by using the specified PARDISO session, where *A* is the matrix specified in the [PARDISO Advanced Initialization](../lvmasmtref/masm_pardiso_adv_init.html) VI or the [PARDISO Advanced Factorization](../lvmasmtref/masm_pardiso_adv_factorization.html) VI.

You must initialize the PARDISO session by using the PARDISO Advanced Initialization VI and performing numerical factorization by using the PARDISO Advanced Factorization VI before solving a sparse linear system.

[Details](#details)

#### PARDISO Advanced Solver (DBL)

[IMAGE alt='image' src='pardiso_advanced_solver__dbl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Vector returns the solution X to AX = Y where A is the matrix specified in PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (SGL)

[IMAGE alt='image' src='pardiso_advanced_solver__sgl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Vector returns the solution X to AX = Y where A is the matrix specified in PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (CDB)

[IMAGE alt='image' src='pardiso_advanced_solver__cdb.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Vector returns the solution X to AX = Y where A is the matrix specified in PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (CSG)

[IMAGE alt='image' src='pardiso_advanced_solver__csg.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the matrix specified in PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Vector returns the solution X to AX = Y where A is the matrix specified in PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (nRHS DBL)

[IMAGE alt='image' src='pardiso_advanced_solver__nrhs_dbl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the matrix specified in the PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Matrix returns the solution X to AX = Y where A is the matrix specified in the PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (nRHS SGL)

[IMAGE alt='image' src='pardiso_advanced_solver__nrhs_sgl.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the matrix specified in the PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Matrix returns the solution X to AX = Y where A is the matrix specified in the PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (nRHS CDB)

[IMAGE alt='image' src='pardiso_advanced_solver__nrhs_cdb.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the matrix specified in the PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Matrix returns the solution X to AX = Y where A is the matrix specified in the PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver (nRHS CSG)

[IMAGE alt='image' src='pardiso_advanced_solver__nrhs_csg.gif']

|  | solver ID in specifies the identification number associated with the PARDISO session. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the matrix specified in the PARDISO Advanced Initialization VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | solver ID out returns solver ID in. |
|  | Solution Matrix returns the solution X to AX = Y where A is the matrix specified in the PARDISO Advanced Initialization VI or PARDISO Advanced Factorization VI and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Advanced Solver Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pardiso_solver.html language=enus -->
## TOPIC 00093: PARDISO Solver VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pardiso_solver.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pardiso_solver.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PARDISO Solver VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Solves a sparse linear system *A**X* = *Y* by using PARDISO.

[Details](#details)

#### PARDISO Solver (DBL)

[IMAGE alt='image' src='pardiso_solver__dbl.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (SGL)

[IMAGE alt='image' src='pardiso_solver__sgl.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (CDB)

[IMAGE alt='image' src='pardiso_solver__cdb.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (CSG)

[IMAGE alt='image' src='pardiso_solver__csg.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (nRHS DBL)

[IMAGE alt='image' src='pardiso_solver__nrhs_dbl.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (nRHS SGL)

[IMAGE alt='image' src='pardiso_solver__nrhs_sgl.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (nRHS CDB)

[IMAGE alt='image' src='pardiso_solver__nrhs_cdb.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver (nRHS CSG)

[IMAGE alt='image' src='pardiso_solver__nrhs_csg.gif']

|  | Input Matrix specifies a square sparse matrix in the sparse linear system to solve. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | matrix type specifies the matrix type of the Input Matrix. 0General (default)—Specifies a square matrix.1Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system.2Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero.3Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 0 | General (default)—Specifies a square matrix. |
| 1 | Symmetric—Specifies a symmetric matrix. LabVIEW only uses the upper triangular part in the Input Matrix to solve the linear system. |
| 2 | Hermitian—Specifies a Hermitian matrix. This option is the same as Symmetric when the Input Matrix is a real-valued matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
| 3 | Positive Definite—Specifies a symmetric positive definite or Hermitian positive definite matrix. LabVIEW only uses the upper triangular part of the Input Matrix to solve the linear system. LabVIEW also considers all diagonal elements in the Input Matrix to have an imaginary part of zero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solver Parameters specifies the set of parameters to use when configuring PARDISO. ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | ordering method specifies the method of permutation in order to reduce fill-in on factorization. 0Minimum Degree—Specifies to use the minimum degree algorithm.1Nested Dissection (default)—Specifies to use the nested dissection algorithm.2Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm.3User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
| 0 | Minimum Degree—Specifies to use the minimum degree algorithm. |
| 1 | Nested Dissection (default)—Specifies to use the nested dissection algorithm. |
| 2 | Parallel Nested Dissection—Specifies to use the parallel version of nested dissection algorithm. |
| 3 | User Defined Permutation—Specifies to use the User Defined Permutation as the permutation vector to reduce fill-in. |
|  | User Defined Permutation specifies the permutation vector to reduce fill-in. LabVIEW uses the user defined permutation vector only when ordering method is User Defined Permutation. |
|  | output permutation? specifies whether LabVIEW returns the permutation vector that PARDISO actually used. The default is FALSE. |
|  | max # of iterative refinement specifies the maximum number of iterative refinement that PARDISO can perform. The default is 0. |
|  | max weighted matching? specifies whether PARDISO uses a maximum weighted matching algorithm to permute large elements close to the diagonal. The default is FALSE. For highly indefinite symmetric matrices, National Instruments recommends setting max weighted matching? to TRUE. |
|  | output MFlops on LU? specifies whether LabVIEW returns the number of floating-point operations in MFlops on factorization. Returning MFlops increases factorization time. The default is FALSE. |
|  | memory option specifies whether LabVIEW uses the in-core or out-of-core (OOC) version of PARDISO. 0Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use.1In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory.2Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
| 0 | Auto—Specifies that LabVIEW automatically determines the version of PARDISO to use. |
| 1 | In Core (default)—Specifies to use the in-core version of PARDISO where LabVIEW stores matrix factors in memory. |
| 2 | Out of Core—Specifies to use the out-of-core version of PARDISO where LabVIEW stores matrix factors in files on hard disk. Use this option for very large problems. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | Diagnostic Info returns diagnostic information. Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. # of nonzeros in LU returns the number of nonzeros in the factorization. peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | Permutation returns the permutation vector that PARDISO actually used. LabVIEW returns the permutation vector only when output permutation? is TRUE. |
|  | # of iterative refinement returns the number of iterative refinement that PARDISO actually performed. |
|  | # of nonzeros in LU returns the number of nonzeros in the factorization. |
|  | peak memory [KB] on symbolic LU returns the peak memory in kilobytes that PARDISO needed on symbolic factorization. |
|  | allocated memory [KB] on symbolic LU returns the memory, in kilobytes, that PARDISO actually allocated on symbolic factorization. |
|  | allocated memory [KB] on LU returns the memory, in kilobytes, that PARDISO actually allocated on numerical factorization. |
|  | MFlops on LU returns the number of floating-point operations, in MFlops, on factorization. LabVIEW returns MFlops only when output MFlops on LU? is TRUE. |
|  | # of positive eigenvalues returns the number of positive eigenvalues when the Input Matrix is symmetric. |
|  | # of negative eigenvalues returns the number of negative eigenvalues when the Input Matrix is symmetric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PARDISO Solver Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_power_spectrum.html language=enus -->
## TOPIC 00094: Power Spectrum VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_power_spectrum.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_power_spectrum.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Power Spectrum VI

**Owning Palette:** [Spectral Analysis VIs](../lvmasmtref/masm_spectral_anls_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the double-sided power spectrum of a time-domain signal **X**.

Wire data to the **X** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Power Spectrum (DBL)

[IMAGE alt='image' src='power_spectrum__dbl.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the double-sided power spectrum of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Power Spectrum (SGL)

[IMAGE alt='image' src='power_spectrum__sgl.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the double-sided power spectrum of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Power Spectrum (CDB)

[IMAGE alt='image' src='power_spectrum__cdb.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the double-sided power spectrum of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Power Spectrum (CSG)

[IMAGE alt='image' src='power_spectrum__csg.gif']

|  | X specifies the input time-domain signal. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Power Spectrum returns the double-sided power spectrum of X. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Power Spectrum Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

This VI computes the double-sided power spectrum using the following equation.

[IMAGE alt='image' src='noloc_eq_dbl_pwr_spectrum.gif']

where *P*<sub>double</sub> is the double-sided **Power Spectrum** and *n* is the size of **X**.

Refer to the [Details](/csh?topicname=lvanls/power_spectrum_sxx.html) section in the [Power Spectrum](/csh?topicname=lvanls/power_spectrum_sxx.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_pseudoinverse_matrix.html language=enus -->
## TOPIC 00095: PseudoInverse Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_pseudoinverse_matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_pseudoinverse_matrix.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PseudoInverse Matrix VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Finds the pseudoinverse of **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### PseudoInverse Matrix (DBL)

[IMAGE alt='image' src='pseudoinverse_matrix__dbl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is not square or singular, the inverse of Input Matrix does not exist. You can compute the pseudoinverse of Input Matrix instead. If Input Matrix is empty, this VI sets PseudoInverse Matrix to an empty matrix. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a double-precision machine epsilon, as shown in the following relationship. = 2–52 = 2.22e – 16 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PseudoInverse Matrix returns the pseudoinverse matrix of the Input Matrix. If Input Matrix is square and nonsingular, the pseudoinverse is the same as the inverse of Input Matrix, and using the Inverse Matrix VI to compute A–1 is more efficient than using this VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PseudoInverse Matrix (SGL)

[IMAGE alt='image' src='pseudoinverse_matrix__sgl.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is not square or singular, the inverse of Input Matrix does not exist. You can compute the pseudoinverse of Input Matrix instead. If Input Matrix is empty, this VI sets PseudoInverse Matrix to an empty matrix. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a single-precision machine epsilon, as shown in the following relationship. = 2–23 = 1.19e – 7 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PseudoInverse Matrix returns the pseudoinverse matrix of the Input Matrix. If Input Matrix is square and nonsingular, the pseudoinverse is the same as the inverse of Input Matrix, and using the Inverse Matrix VI to compute A–1 is more efficient than using this VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PseudoInverse Matrix (CDB)

[IMAGE alt='image' src='pseudoinverse_matrix__cdb.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is not square or singular, the inverse of Input Matrix does not exist. You can compute the pseudoinverse of Input Matrix instead. If Input Matrix is empty, this VI sets PseudoInverse Matrix to an empty matrix. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a double-precision machine epsilon, as shown in the following relationship. = 2–52 = 2.22e – 16 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PseudoInverse Matrix returns the pseudoinverse matrix of the Input Matrix. If Input Matrix is square and nonsingular, the pseudoinverse is the same as the inverse of Input Matrix, and using the Inverse Matrix VI to compute A–1 is more efficient than using this VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PseudoInverse Matrix (CSG)

[IMAGE alt='image' src='pseudoinverse_matrix__csg.gif']

|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is not square or singular, the inverse of Input Matrix does not exist. You can compute the pseudoinverse of Input Matrix instead. If Input Matrix is empty, this VI sets PseudoInverse Matrix to an empty matrix. |
| --- | --- |
|  | tolerance specifies a level such that this VI treats the singular values of Input Matrix that are smaller than or equal to this level as zeros. The default is –1. If tolerance is negative, this VI specifies tolerance according to the following equation. tolerance = max(m,n)*\|\|A\|\|*, where A represents the Input Matrix, \|\|A\|\| is the 2-norm of A, m represents the number of rows in A, n represents the number of columns in A, and is a single-precision machine epsilon, as shown in the following relationship. = 2–23 = 1.19e – 7 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | PseudoInverse Matrix returns the pseudoinverse matrix of the Input Matrix. If Input Matrix is square and nonsingular, the pseudoinverse is the same as the inverse of Input Matrix, and using the Inverse Matrix VI to compute A–1 is more efficient than using this VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PseudoInverse Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/pseudoinverse_matrix.html) section in the [PseudoInverse Matrix](/csh?topicname=gmath/pseudoinverse_matrix.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_qr_decomp.html language=enus -->
## TOPIC 00096: QR Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_qr_decomp.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_qr_decomp.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### QR Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the QR decomposition of a matrix **A**.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### QR Decomposition (DBL)

[IMAGE alt='image' src='qr_decomposition__dbl.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI decomposes A according to the following equation: AP=QR. This VI returns the absolute values of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according to the following equation: A=QR. The default is FALSE. |
|  | Q option specifies how this VI generates Q. 0Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.1Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.2No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
| 0 | Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n. |
| 1 | Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n. |
| 2 | No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Q returns the decomposed Q matrix. The columns of Q compose an orthogonal set. Q is empty if Q option is set to No Q. |
|  | R returns the decomposed upper triangular R matrix. |
|  | P returns the decomposed permutation matrix. P is empty if pivot? is set to FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### QR Decomposition (SGL)

[IMAGE alt='image' src='qr_decomposition__sgl.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI decomposes A according to the following equation: AP=QR. This VI returns the absolute values of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according to the following equation: A=QR. The default is FALSE. |
|  | Q option specifies how this VI generates Q. 0Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.1Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.2No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
| 0 | Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n. |
| 1 | Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n. |
| 2 | No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Q returns the decomposed Q matrix. The columns of Q compose an orthogonal set. Q is empty if Q option is set to No Q. |
|  | R returns the decomposed upper triangular R matrix. |
|  | P returns the decomposed permutation matrix. P is empty if pivot? is set to FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### QR Decomposition (CDB)

[IMAGE alt='image' src='qr_decomposition__cdb.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI decomposes A according to the following equation: AP=QR. This VI returns the absolute values of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according to the following equation: A=QR. The default is FALSE. |
|  | Q option specifies how this VI generates Q. 0Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.1Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.2No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
| 0 | Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n. |
| 1 | Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n. |
| 2 | No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Q returns the decomposed Q matrix. The columns of Q compose an orthogonal set. Q is empty if Q option is set to No Q. |
|  | R returns the decomposed upper triangular R matrix. |
|  | P returns the decomposed permutation matrix. P is empty if pivot? is set to FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### QR Decomposition (CSG)

[IMAGE alt='image' src='qr_decomposition__csg.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | pivot? specifies whether this VI decomposes A with column pivoting. When pivot? is TRUE, this VI decomposes A according to the following equation: AP=QR. This VI returns the absolute values of the diagonals of R in descending order. When pivot? is FALSE, this VI decomposes A according to the following equation: A=QR. The default is FALSE. |
|  | Q option specifies how this VI generates Q. 0Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n.1Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n.2No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
| 0 | Full Size Q (default)—The size of Q is m-by-m, and the size of R is m-by-n. |
| 1 | Economy Size Q—The size of Q is m-by-min(m, n), and the size of R is min(m, n)-by-n. |
| 2 | No Q—This VI does not generate Q, and the size of R is min(m, n)-by-n. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Q returns the decomposed Q matrix. The columns of Q compose an orthogonal set. Q is empty if Q option is set to No Q. |
|  | R returns the decomposed upper triangular R matrix. |
|  | P returns the decomposed permutation matrix. P is empty if pivot? is set to FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### QR Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/qr_decomposition.html) section in the [QR Decomposition](/csh?topicname=gmath/qr_decomposition.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_qz_decomp.html language=enus -->
## TOPIC 00097: QZ Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_qz_decomp.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_qz_decomp.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### QZ Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the QZ decomposition of a pair of matrices **A** and **B**.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### QZ Decomposition (DBL)

[IMAGE alt='image' src='qz_decomposition__dbl.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | decomposition type specifies the type of decomposition. 0Generalized Hessenberg (default)1Generalized Schur |
| 0 | Generalized Hessenberg (default) |
| 1 | Generalized Schur |
|  | order specifies how to order the generalized eigenvalues, Alpha and Beta, and the corresponding Eigenvectors, Q, and Z. order is valid only when decomposition type is Generalized Schur. 0No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues.1Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts.2Real Descending—Lists the generalized eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues. |
| 1 | Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the generalized eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns. |
|  | Q returns an orthogonal matrix. Let trans(Q) represent the transpose matrix of Q, then Q satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Z returns an orthogonal matrix. Let trans(Q) represent the transpose matrix of Q, then Z satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Alpha returns the numerators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | Beta returns the denominators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | error out contains error information. This output provides standard error out functionality. |

#### QZ Decomposition (SGL)

[IMAGE alt='image' src='qz_decomposition__sgl.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | decomposition type specifies the type of decomposition. 0Generalized Hessenberg (default)1Generalized Schur |
| 0 | Generalized Hessenberg (default) |
| 1 | Generalized Schur |
|  | order specifies how to order the generalized eigenvalues, Alpha and Beta, and the corresponding Eigenvectors, Q, and Z. order is valid only when decomposition type is Generalized Schur. 0No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues.1Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts.2Real Descending—Lists the generalized eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues. |
| 1 | Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the generalized eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns. |
|  | Q returns an orthogonal matrix. Let trans(Q) represent the transpose matrix of Q, then Q satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Z returns an orthogonal matrix. Let trans(Q) represent the transpose matrix of Q, then Z satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or a quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal blocks if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Alpha returns the numerators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | Beta returns the denominators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | error out contains error information. This output provides standard error out functionality. |

#### QZ Decomposition (CDB)

[IMAGE alt='image' src='qz_decomposition__cdb.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | decomposition type specifies the type of decomposition. 0Generalized Hessenberg (default)1Generalized Schur |
| 0 | Generalized Hessenberg (default) |
| 1 | Generalized Schur |
|  | order specifies how to order the generalized eigenvalues, Alpha and Beta, and the corresponding Eigenvectors, Q, and Z. order is valid only when decomposition type is Generalized Schur. 0No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues.1Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts.2Real Descending—Lists the generalized eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues. |
| 1 | Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the generalized eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns. |
|  | Q returns a unitary matrix. Let trans(Q) represent the conjugate transpose matrix of Q, then Q satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or an upper triangular matrix if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Z returns a unitary matrix. Let trans(Q) represent the conjugate transpose matrix of Q, then Z satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or an upper triangular matrix if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Alpha returns the numerators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | Beta returns the denominators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | error out contains error information. This output provides standard error out functionality. |

#### QZ Decomposition (CSG)

[IMAGE alt='image' src='qz_decomposition__csg.gif']

|  | A specifies the first square matrix. A and B must be the same size. |
| --- | --- |
|  | B specifies the second square matrix. A and B must be the same size. |
|  | decomposition type specifies the type of decomposition. 0Generalized Hessenberg (default)1Generalized Schur |
| 0 | Generalized Hessenberg (default) |
| 1 | Generalized Schur |
|  | order specifies how to order the generalized eigenvalues, Alpha and Beta, and the corresponding Eigenvectors, Q, and Z. order is valid only when decomposition type is Generalized Schur. 0No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues.1Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts.2Real Descending—Lists the generalized eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (default)—Specifies that this VI does not change the order of the generalized eigenvalues. |
| 1 | Real Ascending—Lists the generalized eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the generalized eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the generalized eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the generalized eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Eigenvectors returns a complex matrix that contains the generalized eigenvectors in its columns. |
|  | Q returns a unitary matrix. Let trans(Q) represent the conjugate transpose matrix of Q, then Q satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or an upper triangular matrix if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Z returns a unitary matrix. Let trans(Q) represent the conjugate transpose matrix of Q, then Z satisfies the following conditions: trans(Q)AZ is an upper Hessenberg matrix if the decomposition type is Generalized Hessenberg; or an upper triangular matrix if the decomposition type is Generalized Schur. trans(Q)BZ is an upper triangular matrix. |
|  | Alpha returns the numerators of the generalized eigenvalues of matrix pair (A, B). If Beta is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | Beta returns the denominators of the generalized eigenvalues of matrix pair (A, B). If Betai is nonzero, Alphai/Betai is a generalized eigenvalue of (A, B). |
|  | error out contains error information. This output provides standard error out functionality. |

#### QZ Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/qz_decomp.html) section in the [QZ Decomposition](/csh?topicname=gmath/qz_decomp.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_re_im_to_complex.html language=enus -->
## TOPIC 00098: Re Im To Complex VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_re_im_to_complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_re_im_to_complex.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Re Im To Complex VI

**Owning Palette:** [Complex VIs](../lvmasmtref/masm_complex_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Creates a complex sparse matrix from two real sparse matrices containing real and imaginary parts, respectively.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Re Im to Complex Sparse Matrix (DBL)

[IMAGE alt='image' src='re_im_to_complex_sparse_matrix__dbl.gif']

|  | A specifies a real sparse matrix containing the real parts to create A + iB. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a real sparse matrix containing the imaginary parts to create A + iB. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A + iB returns a complex sparse matrix with A and B as its real and imaginary parts, respectively. |

#### Re Im to Complex Sparse Matrix (SGL)

[IMAGE alt='image' src='re_im_to_complex_sparse_matrix__sgl.gif']

|  | A specifies a real sparse matrix containing the real parts to create A + iB. The number of rows and columns in A must be equal to the number of rows and columns in B, respectively. |
| --- | --- |
|  | B specifies a real sparse matrix containing the imaginary parts to create A + iB. The number of rows and columns in B must be equal to the number of rows and columns in A, respectively. |
|  | A + iB returns a complex sparse matrix with A and B as its real and imaginary parts, respectively. |

#### Re Im To Complex Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_read_from_matrix_mkt.html language=enus -->
## TOPIC 00099: Read from Matrix Market File VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_read_from_matrix_mkt.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_read_from_matrix_mkt.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read from Matrix Market File VI

**Owning Palette:** [File I/O VIs](../lvmasmtref/masm_file_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Reads a matrix from a file in the Matrix Market exchange format.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use. The [instance you select](#details) and the actual matrix stored in the Matrix Market file must match. Otherwise, LabVIEW returns an error.

[Details](#details)  [Example](#examples)

#### Read Sparse from Matrix Market (DBL)

[IMAGE alt='image' src='read_sparse_from_matrix_market__dbl.gif']

|  | Matrix Market file specifies an absolute path to a file from which you want to read the matrix. |
| --- | --- |
|  | matrix info only? specifies whether to read the value of the matrix elements from Matrix Market file. The default is FALSE, which specifies that this VI reads the value of the matrix elements and the matrix information. When matrix info only? is TRUE, this VI reads the value of the matrix information only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Market file out returns Matrix Market file. |
|  | Sparse Matrix returns the matrix read from Matrix Market file. This output returns an empty matrix when matrix info only? is TRUE. |
|  | matrix info returns the matrix information read from Matrix Market file. format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. number of rows returns the number of rows in Sparse Matrix. number of columns returns the number of columns in Sparse Matrix. number of elements returns the number of elements stored in the file when matrix info only? is TRUE. When matrix info only? is FALSE, number of elements returns the actual number of elements in Sparse Matrix. The actual number of elements can be determined only when all matrix data have been read from the file. description returns the description of the matrix in Matrix Market file. |
|  | format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
| 0 | Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices. |
| 1 | Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
|  | field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
| 0 | Real—The matrix is a real matrix. Elements are represented by a floating number in the file. |
| 1 | Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file. |
| 2 | Integer—The matrix is an integer matrix. Elements are represented an integer. |
| 3 | Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
|  | matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
| 0 | General—The matrix is a general matrix. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | number of elements returns the number of elements stored in the file when matrix info only? is TRUE. When matrix info only? is FALSE, number of elements returns the actual number of elements in Sparse Matrix. The actual number of elements can be determined only when all matrix data have been read from the file. |
|  | description returns the description of the matrix in Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Read Sparse from Matrix Market (CDB)

[IMAGE alt='image' src='read_sparse_from_matrix_market__cdb.gif']

|  | Matrix Market file specifies an absolute path to a file from which you want to read the matrix. |
| --- | --- |
|  | matrix info only? specifies whether to read the value of the matrix elements from Matrix Market file. The default is FALSE, which specifies that this VI reads the value of the matrix elements and the matrix information. When matrix info only? is TRUE, this VI reads the value of the matrix information only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Market file out returns Matrix Market file. |
|  | Sparse Matrix returns the matrix read from Matrix Market file. This output returns an empty matrix when matrix info only? is TRUE. |
|  | matrix info returns the matrix information read from Matrix Market file. format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. number of rows returns the number of rows in Sparse Matrix. number of columns returns the number of columns in Sparse Matrix. number of elements returns the number of elements stored in the file when matrix info only? is TRUE. When matrix info only? is FALSE, number of elements returns the actual number of elements in Sparse Matrix. The actual number of elements can be determined only when all matrix data have been read from the file. description returns the description of the matrix in Matrix Market file. |
|  | format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
| 0 | Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices. |
| 1 | Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
|  | field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
| 0 | Real—The matrix is a real matrix. Elements are represented by a floating number in the file. |
| 1 | Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file. |
| 2 | Integer—The matrix is an integer matrix. Elements are represented an integer. |
| 3 | Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
|  | matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
| 0 | General—The matrix is a general matrix. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
|  | number of rows returns the number of rows in Sparse Matrix. |
|  | number of columns returns the number of columns in Sparse Matrix. |
|  | number of elements returns the number of elements stored in the file when matrix info only? is TRUE. When matrix info only? is FALSE, number of elements returns the actual number of elements in Sparse Matrix. The actual number of elements can be determined only when all matrix data have been read from the file. |
|  | description returns the description of the matrix in Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Read Dense from Matrix Market (DBL)

[IMAGE alt='image' src='read_dense_from_matrix_market__dbl.gif']

|  | Matrix Market file specifies an absolute path to a file from which you want to read the matrix. |
| --- | --- |
|  | matrix info only? specifies whether to read the value of the matrix elements from Matrix Market file. The default is FALSE, which specifies that this VI reads the value of the matrix elements and the matrix information. When matrix info only? is TRUE, this VI reads the value of the matrix information only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Market file out returns Matrix Market file. |
|  | Dense Matrix returns the matrix read from Matrix Market file. This output returns an empty matrix when matrix info only? is TRUE. |
|  | matrix info returns the matrix information read from Matrix Market file. format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. number of rows returns the number of rows in Dense Matrix. number of columns returns the number of columns in Dense Matrix. number of elements returns the number of elements in Dense Matrix. The number of elements is equal to the product of number of rows and number of columns in Dense Matrix. description returns the description of the matrix in Matrix Market file. |
|  | format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
| 0 | Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices. |
| 1 | Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
|  | field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
| 0 | Real—The matrix is a real matrix. Elements are represented by a floating number in the file. |
| 1 | Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file. |
| 2 | Integer—The matrix is an integer matrix. Elements are represented an integer. |
| 3 | Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
|  | matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
| 0 | General—The matrix is a general matrix. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
|  | number of rows returns the number of rows in Dense Matrix. |
|  | number of columns returns the number of columns in Dense Matrix. |
|  | number of elements returns the number of elements in Dense Matrix. The number of elements is equal to the product of number of rows and number of columns in Dense Matrix. |
|  | description returns the description of the matrix in Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Read Dense from Matrix Market (CDB)

[IMAGE alt='image' src='read_dense_from_matrix_market__cdb.gif']

|  | Matrix Market file specifies an absolute path to a file from which you want to read the matrix. |
| --- | --- |
|  | matrix info only? specifies whether to read the value of the matrix elements from Matrix Market file. The default is FALSE, which specifies that this VI reads the value of the matrix elements and the matrix information. When matrix info only? is TRUE, this VI reads the value of the matrix information only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Matrix Market file out returns Matrix Market file. |
|  | Dense Matrix returns the matrix read from Matrix Market file. This output returns an empty matrix when matrix info only? is TRUE. |
|  | matrix info returns the matrix information read from Matrix Market file. format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. number of rows returns the number of rows in Dense Matrix. number of columns returns the number of columns in Dense Matrix. number of elements returns the number of elements in Dense Matrix. The number of elements is equal to the product of number of rows and number of columns in Dense Matrix. description returns the description of the matrix in Matrix Market file. |
|  | format returns the format of the matrix in Matrix Market file. 0Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices.1Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
| 0 | Coordinate—Matrix is formatted in coordinate in the file. This format applies to sparse matrices. |
| 1 | Array—Matrix is formatted in array in the file. This format applies to dense matrices. |
|  | field returns the data type of the matrix and how the Market Matrix file represents the matrix elements. 0Real—The matrix is a real matrix. Elements are represented by a floating number in the file.1Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file.2Integer—The matrix is an integer matrix. Elements are represented an integer.3Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
| 0 | Real—The matrix is a real matrix. Elements are represented by a floating number in the file. |
| 1 | Complex—The matrix is a complex matrix. Elements are represented by two floating numbers, indicating the real and imaginary parts, in the file. |
| 2 | Integer—The matrix is an integer matrix. Elements are represented an integer. |
| 3 | Pattern—The matrix shows its sparsity pattern. Row and column indices of elements are stored in the file. Pattern applies to sparse matrices. |
|  | matrix type returns the type of the matrix and how the Matrix Market file stores matrix elements. 0General—The matrix is a general matrix.1Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file.3Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
| 0 | General—The matrix is a general matrix. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only the lower triangular part is stored in the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only the strict lower triangular part is stored in the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only the lower triangular part is stored in the file. This type applies only to complex matrices. |
|  | number of rows returns the number of rows in Dense Matrix. |
|  | number of columns returns the number of columns in Dense Matrix. |
|  | number of elements returns the number of elements in Dense Matrix. The number of elements is equal to the product of number of rows and number of columns in Dense Matrix. |
|  | description returns the description of the matrix in Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Read from Matrix Market File Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

Refer to the following table to determine the instance to use.

| Instance to use | Format | Field | Type |
| --- | --- | --- | --- |
| Read Sparse from Matrix Market (DBL) | Coordinate | Real | General |
| Integer | Symmetric |  |  |
| Pattern | Skew-symmetric |  |  |
| Read Sparse from Matrix Market (CDB) | Coordinate | Real | General |
| Complex | Symmetric |  |  |
| Integer | Skew-symmetric |  |  |
| Pattern | Hermitian |  |  |
| Read Dense from Matrix Market (DBL) | Array | Real | General |
| Integer | Symmetric |  |  |
| Skew-symmetric |  |  |  |
| Read Dense from Matrix Market (CDB) | Array | Real | General |
| Complex | Symmetric |  |  |
| Integer | Skew-symmetric |  |  |
| Hermitian |  |  |  |

#### Example

Refer to the Read Matrix from Matrix Market File VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Read from Matrix Market File VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_reorder_elements.html language=enus -->
## TOPIC 00100: Reorder Elements VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_reorder_elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_reorder_elements.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Reorder Elements VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Reorders elements in a sparse matrix according to their row and column indices. Reordering elements in a sparse matrix usually speeds up sparse matrix operations.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Reorder Sparse Matrix Elements (DBL)

[IMAGE alt='image' src='reorder_sparse_matrix_elements__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in Sparse Matrix according to their row and column indices. 0No Reorder—Specifies that this VI does not reorder elements in a certain order.1Row—Specifies that this VI reorders elements in order of ascending row indices.2Column—Specifies that this VI reorders elements in order of ascending column indices.3Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder—Specifies that this VI does not reorder elements in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in order of ascending column indices. |
| 3 | Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Reordered Sparse Matrix returns Sparse Matrix with elements reordered according to their row and column indices. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reorder Sparse Matrix Elements (SGL)

[IMAGE alt='image' src='reorder_sparse_matrix_elements__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in Sparse Matrix according to their row and column indices. 0No Reorder—Specifies that this VI does not reorder elements in a certain order.1Row—Specifies that this VI reorders elements in order of ascending row indices.2Column—Specifies that this VI reorders elements in order of ascending column indices.3Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder—Specifies that this VI does not reorder elements in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in order of ascending column indices. |
| 3 | Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Reordered Sparse Matrix returns Sparse Matrix with elements reordered according to their row and column indices. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reorder Sparse Matrix Elements (CDB)

[IMAGE alt='image' src='reorder_sparse_matrix_elements__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in Sparse Matrix according to their row and column indices. 0No Reorder—Specifies that this VI does not reorder elements in a certain order.1Row—Specifies that this VI reorders elements in order of ascending row indices.2Column—Specifies that this VI reorders elements in order of ascending column indices.3Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder—Specifies that this VI does not reorder elements in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in order of ascending column indices. |
| 3 | Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Reordered Sparse Matrix returns Sparse Matrix with elements reordered according to their row and column indices. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reorder Sparse Matrix Elements (CSG)

[IMAGE alt='image' src='reorder_sparse_matrix_elements__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | order specifies how to reorder elements in Sparse Matrix according to their row and column indices. 0No Reorder—Specifies that this VI does not reorder elements in a certain order.1Row—Specifies that this VI reorders elements in order of ascending row indices.2Column—Specifies that this VI reorders elements in order of ascending column indices.3Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices.4Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
| 0 | No Reorder—Specifies that this VI does not reorder elements in a certain order. |
| 1 | Row—Specifies that this VI reorders elements in order of ascending row indices. |
| 2 | Column—Specifies that this VI reorders elements in order of ascending column indices. |
| 3 | Row and Column (default)—Specifies that this VI reorders elements in order of ascending row indices and then ascending column indices. |
| 4 | Column and Row—Specifies that this VI reorders elements in order of ascending column indices and then ascending row indices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Reordered Sparse Matrix returns Sparse Matrix with elements reordered according to their row and column indices. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Reorder Elements Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_schur_decomp.html language=enus -->
## TOPIC 00101: Schur Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_schur_decomp.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_schur_decomp.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Schur Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the Schur decomposition of the **Input Matrix**.

Wire data to the **Input Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Schur Decomposition (DBL)

[IMAGE alt='image' src='schur_decomposition__dbl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | compute Schur vectors? specifies whether this VI computes Schur Vectors. The default is FALSE. |
|  | order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur Vectors. 0No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues.1Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.2Real Descending—Lists the Eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues. |
| 1 | Real Ascending—Lists the Eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the Eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Schur Form returns the decomposed block upper triangular matrix in real Schur form. |
|  | Schur Vectors returns the decomposed orthogonal matrix. Schur Vectors is empty if compute Schur vectors? is set to FALSE. |
|  | Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Schur Decomposition (SGL)

[IMAGE alt='image' src='schur_decomposition__sgl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | compute Schur vectors? specifies whether this VI computes Schur Vectors. The default is FALSE. |
|  | order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur Vectors. 0No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues.1Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.2Real Descending—Lists the Eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues. |
| 1 | Real Ascending—Lists the Eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the Eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Schur Form returns the decomposed block upper triangular matrix in real Schur form. |
|  | Schur Vectors returns the decomposed orthogonal matrix. Schur Vectors is empty if compute Schur vectors? is set to FALSE. |
|  | Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Schur Decomposition (CDB)

[IMAGE alt='image' src='schur_decomposition__cdb.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | compute Schur vectors? specifies whether this VI computes Schur Vectors. The default is FALSE. |
|  | order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur Vectors. 0No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues.1Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.2Real Descending—Lists the Eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues. |
| 1 | Real Ascending—Lists the Eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the Eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Schur Form returns the decomposed upper triangular matrix. |
|  | Schur Vectors returns the decomposed unitary matrix. Schur Vectors is empty if compute Schur vectors? is set to FALSE |
|  | Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Schur Decomposition (CSG)

[IMAGE alt='image' src='schur_decomposition__csg.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | compute Schur vectors? specifies whether this VI computes Schur Vectors. The default is FALSE. |
|  | order specifies how to order the Eigenvalues and the corresponding Schur Form and Schur Vectors. 0No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues.1Real Ascending—Lists the Eigenvalues in ascending order according to their real parts.2Real Descending—Lists the Eigenvalues in descending order according to their real parts.3Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes.4Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
| 0 | No Reorder (Default)—Specifies that this VI does not change the order of the Eigenvalues. |
| 1 | Real Ascending—Lists the Eigenvalues in ascending order according to their real parts. |
| 2 | Real Descending—Lists the Eigenvalues in descending order according to their real parts. |
| 3 | Magnitude Ascending—Lists the Eigenvalues in ascending order according to their magnitudes. |
| 4 | Magnitude Descending—Lists the Eigenvalues in descending order according to their magnitudes. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Schur Form returns the decomposed upper triangular matrix. |
|  | Schur Vectors returns the decomposed unitary matrix. Schur Vectors is empty if compute Schur vectors? is set to FALSE |
|  | Eigenvalues returns a complex vector that contains all the computed eigenvalues of Input Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Schur Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/schur_decomp.html) section in the [Schur Decomposition](/csh?topicname=gmath/schur_decomp.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_set_matrix_size.html language=enus -->
## TOPIC 00102: Set Matrix Size VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_set_matrix_size.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_set_matrix_size.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Matrix Size VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Sets the number of rows and columns in a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Set Sparse Matrix Size (DBL)

[IMAGE alt='image' src='set_sparse_matrix_size__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | number of rows specifies the number of rows to set in Sparse Matrix in. If number of rows is negative, LabVIEW does not change the number of rows in Sparse Matrix in. The default is -1. |
|  | number of columns specifies the number of columns to set in Sparse Matrix in. If number of columns is negative, LabVIEW does not change the number of columns in Sparse Matrix in. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the number of rows and columns you specify in number of rows and number of columns, respectively. If any elements in Sparse Matrix in have a row or column index that is larger than number of rows and number of columns, respectively, LabVIEW removes those elements from Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Size (SGL)

[IMAGE alt='image' src='set_sparse_matrix_size__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | number of rows specifies the number of rows to set in Sparse Matrix in. If number of rows is negative, LabVIEW does not change the number of rows in Sparse Matrix in. The default is -1. |
|  | number of columns specifies the number of columns to set in Sparse Matrix in. If number of columns is negative, LabVIEW does not change the number of columns in Sparse Matrix in. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the number of rows and columns you specify in number of rows and number of columns, respectively. If any elements in Sparse Matrix in have a row or column index that is larger than number of rows and number of columns, respectively, LabVIEW removes those elements from Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Size (CDB)

[IMAGE alt='image' src='set_sparse_matrix_size__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | number of rows specifies the number of rows to set in Sparse Matrix in. If number of rows is negative, LabVIEW does not change the number of rows in Sparse Matrix in. The default is -1. |
|  | number of columns specifies the number of columns to set in Sparse Matrix in. If number of columns is negative, LabVIEW does not change the number of columns in Sparse Matrix in. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the number of rows and columns you specify in number of rows and number of columns, respectively. If any elements in Sparse Matrix in have a row or column index that is larger than number of rows and number of columns, respectively, LabVIEW removes those elements from Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Size (CSG)

[IMAGE alt='image' src='set_sparse_matrix_size__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | number of rows specifies the number of rows to set in Sparse Matrix in. If number of rows is negative, LabVIEW does not change the number of rows in Sparse Matrix in. The default is -1. |
|  | number of columns specifies the number of columns to set in Sparse Matrix in. If number of columns is negative, LabVIEW does not change the number of columns in Sparse Matrix in. The default is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the number of rows and columns you specify in number of rows and number of columns, respectively. If any elements in Sparse Matrix in have a row or column index that is larger than number of rows and number of columns, respectively, LabVIEW removes those elements from Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Matrix Size Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_set_matrix_subset.html language=enus -->
## TOPIC 00103: Set Matrix Subset VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_set_matrix_subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_set_matrix_subset.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Matrix Subset VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Sets a subset in a sparse matrix.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Set Sparse Matrix Element (DBL)

[IMAGE alt='image' src='set_sparse_matrix_element__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index at which LabVIEW sets new element. The row index must be non-negative. The default is 0. |
|  | column index specifies the row index at which LabVIEW sets new element. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new element specifies the element to set at row index and column index. |
|  | Sparse Matrix out returns Sparse Matrix in with new element. If Sparse Matrix in already has an element at row index and column index, LabVIEW replaces the element with new element. Otherwise, LabVIEW adds new element into Sparse Matrix out. If row index or column index is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive new element at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Element (SGL)

[IMAGE alt='image' src='set_sparse_matrix_element__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index at which LabVIEW sets new element. The row index must be non-negative. The default is 0. |
|  | column index specifies the row index at which LabVIEW sets new element. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new element specifies the element to set at row index and column index. |
|  | Sparse Matrix out returns Sparse Matrix in with new element. If Sparse Matrix in already has an element at row index and column index, LabVIEW replaces the element with new element. Otherwise, LabVIEW adds new element into Sparse Matrix out. If row index or column index is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive new element at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Element (CDB)

[IMAGE alt='image' src='set_sparse_matrix_element__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index at which LabVIEW sets new element. The row index must be non-negative. The default is 0. |
|  | column index specifies the row index at which LabVIEW sets new element. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new element specifies the element to set at row index and column index. |
|  | Sparse Matrix out returns Sparse Matrix in with new element. If Sparse Matrix in already has an element at row index and column index, LabVIEW replaces the element with new element. Otherwise, LabVIEW adds new element into Sparse Matrix out. If row index or column index is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive new element at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Element (CSG)

[IMAGE alt='image' src='set_sparse_matrix_element__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the row index at which LabVIEW sets new element. The row index must be non-negative. The default is 0. |
|  | column index specifies the row index at which LabVIEW sets new element. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | new element specifies the element to set at row index and column index. |
|  | Sparse Matrix out returns Sparse Matrix in with new element. If Sparse Matrix in already has an element at row index and column index, LabVIEW replaces the element with new element. Otherwise, LabVIEW adds new element into Sparse Matrix out. If row index or column index is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive new element at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Multi Elem (DBL)

[IMAGE alt='image' src='set_sparse_matrix_multi_elem__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies an array of row indices at which LabVIEW sets New Elements. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative. |
|  | Column Indices specifies an array of column indices at which LabVIEW sets New Elements. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Elements specifies an array of elements to set at Row Indices and Column Indices. The number of elements in New Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | Sparse Matrix out returns Sparse Matrix in with New Elements. If Sparse Matrix in already has elements at Row Indices and Column Indices, LabVIEW replaces the elements with New Elements. Otherwise, LabVIEW adds New Elements into Sparse Matrix out. If Row Indices or Column Indices is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive New Elements at the corresponding position. If two or more elements have identical row and column indices, LabVIEW receives the last element of New Elements in Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Multi Elem (SGL)

[IMAGE alt='image' src='set_sparse_matrix_multi_elem__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies an array of row indices at which LabVIEW sets New Elements. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative. |
|  | Column Indices specifies an array of column indices at which LabVIEW sets New Elements. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Elements specifies an array of elements to set at Row Indices and Column Indices. The number of elements in New Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | Sparse Matrix out returns Sparse Matrix in with New Elements. If Sparse Matrix in already has elements at Row Indices and Column Indices, LabVIEW replaces the elements with New Elements. Otherwise, LabVIEW adds New Elements into Sparse Matrix out. If Row Indices or Column Indices is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive New Elements at the corresponding position. If two or more elements have identical row and column indices, LabVIEW receives the last element of New Elements in Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Multi Elem (CDB)

[IMAGE alt='image' src='set_sparse_matrix_multi_elem__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies an array of row indices at which LabVIEW sets New Elements. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative. |
|  | Column Indices specifies an array of column indices at which LabVIEW sets New Elements. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Elements specifies an array of elements to set at Row Indices and Column Indices. The number of elements in New Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | Sparse Matrix out returns Sparse Matrix in with New Elements. If Sparse Matrix in already has elements at Row Indices and Column Indices, LabVIEW replaces the elements with New Elements. Otherwise, LabVIEW adds New Elements into Sparse Matrix out. If Row Indices or Column Indices is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive New Elements at the corresponding position. If two or more elements have identical row and column indices, LabVIEW receives the last element of New Elements in Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Multi Elem (CSG)

[IMAGE alt='image' src='set_sparse_matrix_multi_elem__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | Row Indices specifies an array of row indices at which LabVIEW sets New Elements. The number of elements in Row Indices must be equal to the number of elements in Column Indices. All elements in Row Indices must be non-negative. |
|  | Column Indices specifies an array of column indices at which LabVIEW sets New Elements. The number of elements in Column Indices must be equal to the number of elements in Row Indices. All elements in Column Indices must be non-negative. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Elements specifies an array of elements to set at Row Indices and Column Indices. The number of elements in New Elements must be equal to the number of elements in Row Indices and Column Indices. |
|  | Sparse Matrix out returns Sparse Matrix in with New Elements. If Sparse Matrix in already has elements at Row Indices and Column Indices, LabVIEW replaces the elements with New Elements. Otherwise, LabVIEW adds New Elements into Sparse Matrix out. If Row Indices or Column Indices is greater than or equal to the number of rows or columns in Sparse Matrix in, LabVIEW resizes Sparse Matrix out to receive New Elements at the corresponding position. If two or more elements have identical row and column indices, LabVIEW receives the last element of New Elements in Sparse Matrix out. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Row (DBL)

[IMAGE alt='image' src='set_sparse_matrix_row__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index at which LabVIEW sets New Row. The row index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Row specifies the row to set at row index. The number of elements in New Row must be equal to the number of columns in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Row. If Sparse Matrix in already has a row at row index, LabVIEW replaces the row with New Row. Otherwise, LabVIEW adds New Row to Sparse Matrix out. If row index is greater than or equal to the number of rows in Sparse Matrix in, LabVIEW appends New Row to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Row (SGL)

[IMAGE alt='image' src='set_sparse_matrix_row__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index at which LabVIEW sets New Row. The row index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Row specifies the row to set at row index. The number of elements in New Row must be equal to the number of columns in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Row. If Sparse Matrix in already has a row at row index, LabVIEW replaces the row with New Row. Otherwise, LabVIEW adds New Row to Sparse Matrix out. If row index is greater than or equal to the number of rows in Sparse Matrix in, LabVIEW appends New Row to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Row (CDB)

[IMAGE alt='image' src='set_sparse_matrix_row__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index at which LabVIEW sets New Row. The row index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Row specifies the row to set at row index. The number of elements in New Row must be equal to the number of columns in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Row. If Sparse Matrix in already has a row at row index, LabVIEW replaces the row with New Row. Otherwise, LabVIEW adds New Row to Sparse Matrix out. If row index is greater than or equal to the number of rows in Sparse Matrix in, LabVIEW appends New Row to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Row (CSG)

[IMAGE alt='image' src='set_sparse_matrix_row__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | row index specifies the index at which LabVIEW sets New Row. The row index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Row specifies the row to set at row index. The number of elements in New Row must be equal to the number of columns in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Row. If Sparse Matrix in already has a row at row index, LabVIEW replaces the row with New Row. Otherwise, LabVIEW adds New Row to Sparse Matrix out. If row index is greater than or equal to the number of rows in Sparse Matrix in, LabVIEW appends New Row to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Column (DBL)

[IMAGE alt='image' src='set_sparse_matrix_column__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index at which LabVIEW sets New Column. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Column specifies the column to set at column index. The number of elements in New Column must be equal to the number of rows in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Column. If Sparse Matrix in already has a column at column index, LabVIEW replaces the column with New Column. Otherwise, LabVIEW adds New Column to Sparse Matrix out. If column index is greater than or equal to the number of columns in Sparse Matrix in, LabVIEW appends New Column to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Column (SGL)

[IMAGE alt='image' src='set_sparse_matrix_column__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index at which LabVIEW sets New Column. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Column specifies the column to set at column index. The number of elements in New Column must be equal to the number of rows in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Column. If Sparse Matrix in already has a column at column index, LabVIEW replaces the column with New Column. Otherwise, LabVIEW adds New Column to Sparse Matrix out. If column index is greater than or equal to the number of columns in Sparse Matrix in, LabVIEW appends New Column to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Column (CDB)

[IMAGE alt='image' src='set_sparse_matrix_column__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index at which LabVIEW sets New Column. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Column specifies the column to set at column index. The number of elements in New Column must be equal to the number of rows in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Column. If Sparse Matrix in already has a column at column index, LabVIEW replaces the column with New Column. Otherwise, LabVIEW adds New Column to Sparse Matrix out. If column index is greater than or equal to the number of columns in Sparse Matrix in, LabVIEW appends New Column to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Column (CSG)

[IMAGE alt='image' src='set_sparse_matrix_column__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | column index specifies the index at which LabVIEW sets New Column. The column index must be non-negative. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | New Column specifies the column to set at column index. The number of elements in New Column must be equal to the number of rows in Sparse Matrix in. |
|  | Sparse Matrix out returns Sparse Matrix in with New Column. If Sparse Matrix in already has a column at column index, LabVIEW replaces the column with New Column. Otherwise, LabVIEW adds New Column to Sparse Matrix out. If column index is greater than or equal to the number of columns in Sparse Matrix in, LabVIEW appends New Column to Sparse Matrix out at the corresponding position. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Matrix Subset Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

##### Setting an Element or Multiple Elements

LabVIEW sets new elements into a sparse matrix even if the elements are explicitly zeros.

##### Setting a Row or Column

LabVIEW sets only non-zero elements in a new row or new column into a sparse matrix. LabVIEW does not receive zero elements in a new row or new column into the output sparse matrix.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_set_max_num_nonzeros.html language=enus -->
## TOPIC 00104: Set Max Number of Nonzeros VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_set_max_num_nonzeros.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_set_max_num_nonzeros.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Max Number of Nonzeros VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Sets the maximum number of nonzeros in a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Set Sparse Matrix Max NZ (DBL)

[IMAGE alt='image' src='set_sparse_matrix_max_nz__dbl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | max number of nonzeros specifies the maximum number of nonzeros to set in Sparse Matrix in. If max number of nonzeros is smaller than the number of elements in Sparse Matrix in, LabVIEW does not change the maximum number of nonzeros. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the maximum number of nonzeros you specify in max number of nonzeros. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Max NZ (SGL)

[IMAGE alt='image' src='set_sparse_matrix_max_nz__sgl.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | max number of nonzeros specifies the maximum number of nonzeros to set in Sparse Matrix in. If max number of nonzeros is smaller than the number of elements in Sparse Matrix in, LabVIEW does not change the maximum number of nonzeros. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the maximum number of nonzeros you specify in max number of nonzeros. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Max NZ (CDB)

[IMAGE alt='image' src='set_sparse_matrix_max_nz__cdb.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | max number of nonzeros specifies the maximum number of nonzeros to set in Sparse Matrix in. If max number of nonzeros is smaller than the number of elements in Sparse Matrix in, LabVIEW does not change the maximum number of nonzeros. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the maximum number of nonzeros you specify in max number of nonzeros. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Sparse Matrix Max NZ (CSG)

[IMAGE alt='image' src='set_sparse_matrix_max_nz__csg.gif']

|  | Sparse Matrix in specifies the input sparse matrix. |
| --- | --- |
|  | max number of nonzeros specifies the maximum number of nonzeros to set in Sparse Matrix in. If max number of nonzeros is smaller than the number of elements in Sparse Matrix in, LabVIEW does not change the maximum number of nonzeros. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Sparse Matrix out returns Sparse Matrix in with the maximum number of nonzeros you specify in max number of nonzeros. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Max Number of Nonzeros Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_set_num_threads.html language=enus -->
## TOPIC 00105: Set Number of Threads VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_set_num_threads.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_set_num_threads.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Number of Threads VI

**Owning Palette:** [Thread Management VIs](../lvmasmtref/masm_thread_mgmt.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Sets the maximum number of threads for parallelism.

LabVIEW does not guarantee that the number of threads you set is used in calculations. The actual number of threads that LabVIEW uses depends on the problem size, system resources, and other considerations. By default, the [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VIs use the number of physical cores as the maximum number of threads unless you specify a smaller number.

This VI is not available on real-time operating systems.

[Details](#details)

[IMAGE alt='image' src='set_number_of_threads.gif']

|  | function domain specifies the domain of functions for which to set the number of threads. 0Default (default)—Sets the default maximum number of threads that applies to all functions. This option does not apply to all functions if you previously specify Linear Algebra or Transform for function domain. Refer to the Details section for more details about this option.1Linear Algebra—Sets the maximum number of threads that applies to linear algebra functions.2Transform—Sets the maximum number of threads that applies to transform functions. |
| --- | --- |
| 0 | Default (default)—Sets the default maximum number of threads that applies to all functions. This option does not apply to all functions if you previously specify Linear Algebra or Transform for function domain. Refer to the Details section for more details about this option. |
| 1 | Linear Algebra—Sets the maximum number of threads that applies to linear algebra functions. |
| 2 | Transform—Sets the maximum number of threads that applies to transform functions. |
|  | number of threads specifies the maximum number of threads for parallelism in function domain. The number of threads must range from 1 to the number of physical cores. The default is 1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Set Number of Threads Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | No |
| --- | --- |

When you specify **function domain**, the **Linear Algebra** and **Transform** options take precedence over the **Default** option, as the following examples demonstrate.

##### Example 1

The following figure demonstrates how to specify two threads for linear algebra functions and one thread for all other functions except linear algebra functions. This figure supposes that the VI runs on a quad-core system.

[IMAGE alt='image' src='masm_set_num_threads_example_1.gif']

By specifying the **function domain** as **Linear Algebra** and specifying the **number of threads** as 2 in the Set Number of Threads VI on the left, the number of threads to use for linear algebra functions is two. You can specify a different number of threads to use for all other functions except linear algebra functions by adding another instance of the Set Number of Threads VI to the block diagram. In the previous figure, the Set Number of Threads VI on the right specifies the **function domain** as **Default** and specifies the **number of threads** as 1. Therefore, the number of threads to use for all functions except linear algebra functions is one. You can use the [Get Number of Threads](../lvmasmtref/masm_get_num_threads.html#details) VI to get the number of threads for each function domain, as the following table shows:

| Function Domain | Number of Threads |
| --- | --- |
| Default | 1 |
| Linear Algebra | 2 |
| Transform | 1 |

##### Example 2

The following figure demonstrates how to specify one thread for linear algebra functions and two threads for transform functions. This figure supposes that the VI runs on a quad-core system.

[IMAGE alt='image' src='masm_set_num_threads_example_2.gif']

By specifying the **function domain** as **Linear Algebra** and specifying the **number of threads** as 1 in the Set Number of Threads VI on the left, the number of threads for linear algebra functions is one. You can specify a different number of threads to use for all other functions except linear algebra functions by adding another instance of the Set Number of Threads VI to the block diagram. In the previous figure, the Set Number of Threads VI on the right specifies the **function domain** as **Transform** and specifies the **number of threads** as 2. Therefore, the number of threads to use for linear algebra functions is one and the number of threads for transform functions is two. The number of threads for all functions other than linear algebra and transform functions remains four. You can use the [Get Number of Threads](../lvmasmtref/masm_get_num_threads.html#details) VI to get the number of threads for each function domain, as the following table shows:

| Function Domain | Number of Threads |
| --- | --- |
| Default | 4 |
| Linear Algebra | 1 |
| Transform | 2 |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_signal_operation_vis.html language=enus -->
## TOPIC 00106: Signal Operation VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_signal_operation_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_signal_operation_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Signal Operation VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Signal Operation VIs to manipulate signals and return a signal output.

| Palette Object | Description |
| --- | --- |
| Auto Correlation | Computes the auto correlation of the input sequence X. |
| Convolution | Computes the convolution of the input sequences X and Y. |
| Cross Correlation | Computes the cross correlation of the input sequences X and Y. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_solve_lin_eq.html language=enus -->
## TOPIC 00107: Solve Linear Equations VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_solve_lin_eq.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_solve_lin_eq.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Solve Linear Equations VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Finds the solution to a linear system AX = Y.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)

#### Solve Least Squares Problems (DBL)

[IMAGE alt='image' src='solve_least_squares_problems__dbl.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a double-precision machine epsilon, as should in the following equation. =2-52=2.22e-16 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (SGL)

[IMAGE alt='image' src='solve_least_squares_problems__sgl.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a single-precision machine epsilon, as should in the following equation. =2-23=1.19e-7 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (CDB)

[IMAGE alt='image' src='solve_least_squares_problems__cdb.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a double-precision machine epsilon, as should in the following equation. =2-52=2.22e-16 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (CSG)

[IMAGE alt='image' src='solve_least_squares_problems__csg.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a single-precision machine epsilon, as should in the following equation. =2-23=1.19e-7 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (nRHS, DBL)

[IMAGE alt='image' src='solve_least_squares_problems__nrhs_dbl.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a double-precision machine epsilon, as should in the following equation. =2-52=2.22e-16 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (nRHS, SGL)

[IMAGE alt='image' src='solve_least_squares_problems__nrhs_sgl.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a single-precision machine epsilon, as should in the following equation. =2-23=1.19e-7 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (nRHS, CDB)

[IMAGE alt='image' src='solve_least_squares_problems__nrhs_cdb.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a double-precision machine epsilon, as should in the following equation. =2-52=2.22e-16 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Least Squares Problems (nRHS, CSG)

[IMAGE alt='image' src='solve_least_squares_problems__nrhs_csg.gif']

|  | relative tolerance specifies a level such that the number of singular values greater than relative tolerance*max(m, n)*\|\|A\|\| is the rank of Input Matrix, where A represents the Input Matrix, \|\|A\|\| represents the 2-norm of A, m represents the number of rows in A, and n represents the number of columns in A. The default is -1. If relative tolerance is negative, the internal relative tolerance used to determine rank is , where is a single-precision machine epsilon, as should in the following equation. =2-23=1.19e-7 |
| --- | --- |
|  | Input Matrix specifies a square or rectangular matrix. If Input Matrix is square and nonsingular, the Least Squares solution is the same as the linear solution to the system, and using Solve Linear Equations instance VIs is more efficient than using this instance VI. |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the Least Square solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (DBL)

[IMAGE alt='image' src='solve_linear_equations__dbl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Vector and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (SGL)

[IMAGE alt='image' src='solve_linear_equations__sgl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Vector and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (CDB)

[IMAGE alt='image' src='solve_linear_equations__cdb.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Vector and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (CSG)

[IMAGE alt='image' src='solve_linear_equations__csg.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Vector specifies an array of known, dependent-variable values. The number of elements in Known Vector must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Vector and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive Definite2Lower Triangular3Upper Triangular |
| 0 | General (default) |
| 1 | Positive Definite |
| 2 | Lower Triangular |
| 3 | Upper Triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (nRHS, DBL)

[IMAGE alt='image' src='solve_linear_equations__nrhs_dbl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Matrix and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive definite2Lower triangular3Upper triangular |
| 0 | General (default) |
| 1 | Positive definite |
| 2 | Lower triangular |
| 3 | Upper triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (nRHS, SGL)

[IMAGE alt='image' src='solve_linear_equations__nrhs_sgl.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Matrix and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive definite2Lower triangular3Upper triangular |
| 0 | General (default) |
| 1 | Positive definite |
| 2 | Lower triangular |
| 3 | Upper triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (nRHS, CDB)

[IMAGE alt='image' src='solve_linear_equations__nrhs_cdb.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Matrix and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive definite2Lower triangular3Upper triangular |
| 0 | General (default) |
| 1 | Positive definite |
| 2 | Lower triangular |
| 3 | Upper triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations (nRHS, CSG)

[IMAGE alt='image' src='solve_linear_equations__nrhs_csg.gif']

|  | Input Matrix specifies a square matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known, dependent-variable values. The number of rows in Known Matrix must be equal to the number of rows in Input Matrix. |
|  | matrix type specifies the type of Input Matrix. Knowing the type of Input Matrix can speed up the computation of the Solution Matrix and can help you to avoid unnecessary computation, which could introduce numerical inaccuracy. 0General (default)1Positive definite2Lower triangular3Upper triangular |
| 0 | General (default) |
| 1 | Positive definite |
| 2 | Lower triangular |
| 3 | Upper triangular |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the linear solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Linear Equations Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances and cases are exceptions: Solve Linear Equations (DBL) Solve Linear Equations (CSG) when matrix type is Positive Definite Solve Linear Equations (nRHS, DBL) Solve Linear Equations (nRHS, CSG) when matrix type is Positive Definite |

Refer to the [Details](/csh?topicname=gmath/solve_linear_equations.html) section in the [Solve Linear Equations](/csh?topicname=gmath/solve_linear_equations.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_solve_triangular_eq.html language=enus -->
## TOPIC 00108: Solve Triangular Equations VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_solve_triangular_eq.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_solve_triangular_eq.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Solve Triangular Equations VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Solves a sparse linear system AX = Y by forward or backward substitution, where A must be a triangular matrix.

[Details](#details)

#### Solve Triangular Equations (DBL)

[IMAGE alt='image' src='solve_triangular_equations__dbl.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of elements in Known Vector must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (SGL)

[IMAGE alt='image' src='solve_triangular_equations__sgl.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of elements in Known Vector must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (CDB)

[IMAGE alt='image' src='solve_triangular_equations__cdb.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of elements in Known Vector must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (CSG)

[IMAGE alt='image' src='solve_triangular_equations__csg.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of elements in Known Vector must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Vector specifies an array of known values. The number of elements in the Known Vector must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Vector returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (nRHS DBL)

[IMAGE alt='image' src='solve_triangular_equations__nrhs_dbl.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of row in Known Matrix must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (nRHS SGL)

[IMAGE alt='image' src='solve_triangular_equations__nrhs_sgl.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of row in Known Matrix must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (nRHS CDB)

[IMAGE alt='image' src='solve_triangular_equations__nrhs_cdb.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of row in Known Matrix must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations (nRHS CSG)

[IMAGE alt='image' src='solve_triangular_equations__nrhs_csg.gif']

|  | Input Matrix specifies the input sparse triangular matrix. Input Matrix must be square. The number of row in Known Matrix must be equal to the number of rows and columns in Input Matrix. |
| --- | --- |
|  | Known Matrix specifies a matrix of known values. The number of rows in the Known Matrix must be equal to the number of rows and columns in the Input Matrix. |
|  | triangular type specifies whether Input Matrix is a lower or upper triangular matrix. 2Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part.3Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
| 2 | Lower Triangular—Specifies that Input Matrix is a lower triangular matrix. LabVIEW does not use the elements in the strict upper triangular part. |
| 3 | Upper Triangular (default)—Specifies that Input Matrix is an upper triangular matrix. LabVIEW does not use the elements in the strict lower triangular part. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Solution Matrix returns the solution X to AX = Y where A is the Input Matrix and Y is the Known Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Solve Triangular Equations Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_sparse_lin_algebra_vis.html language=enus -->
## TOPIC 00109: Sparse Linear Algebra VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_sparse_lin_algebra_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_sparse_lin_algebra_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Sparse Linear Algebra VIs

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Sparse Linear Algebra VIs to perform linear algebra computations and analysis on sparse matrices.

| Palette Object | Description |
| --- | --- |
| A x B | Computes the multiplication of two sparse matrices, a sparse matrix and a dense matrix, or a sparse matrix and a vector. |
| Create Random Matrix | Generates a sparse matrix randomly. |
| Create Special Matrix | Creates a sparse matrix of a specific type. |
| PARDISO Advanced Cleaning Up | Cleans up the specified PARDISO session. You must clean up the session when you no longer use it. |
| PARDISO Advanced Factorization | Performs numerical factorization on the specified PARDISO session. |
| PARDISO Advanced Initialization | Initializes a PARDISO session, attaches a sparse matrix to the initialized session, and analyzes and performs symbolic factorization on the sparse matrix. The PARDISO Advanced Factorization VI uses the analysis result for numerical factorization. |
| PARDISO Advanced Solver | Solves a sparse linear system AX = Y by using the specified PARDISO session, where A is the matrix specified in the PARDISO Advanced Initialization VI or the PARDISO Advanced Factorization VI. |
| PARDISO Solver | Solves a sparse linear system AX = Y by using PARDISO. |
| Solve Triangular Equations | Solves a sparse linear system AX = Y by forward or backward substitution, where A must be a triangular matrix. |
| Trace | Calculates the trace of a sparse matrix. |
| Transpose Matrix | Transposes a sparse matrix. If the matrix is a complex sparse matrix, this VI performs conjugate transposition. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_sparse_to_dense.html language=enus -->
## TOPIC 00110: Sparse to Dense VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_sparse_to_dense.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_sparse_to_dense.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Sparse to Dense VI

**Owning Palette:** [Matrix VIs](../lvmasmtref/masm_matrix_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts a sparse matrix to a dense matrix that contains zero elements explicitly.

If the size of the sparse matrix is too large, LabVIEW might have insufficient memory to convert the sparse matrix to a dense matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Sparse to Dense (DBL)

[IMAGE alt='image' src='sparse_to_dense__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Dense Matrix returns the dense matrix that this VI converts from Sparse Matrix that contains zero elements explicitly. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse to Dense (SGL)

[IMAGE alt='image' src='sparse_to_dense__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Dense Matrix returns the dense matrix that this VI converts from Sparse Matrix that contains zero elements explicitly. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse to Dense (CDB)

[IMAGE alt='image' src='sparse_to_dense__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Dense Matrix returns the dense matrix that this VI converts from Sparse Matrix that contains zero elements explicitly. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse to Dense (CSG)

[IMAGE alt='image' src='sparse_to_dense__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Dense Matrix returns the dense matrix that this VI converts from Sparse Matrix that contains zero elements explicitly. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Sparse to Dense Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_spectral_anls_vis.html language=enus -->
## TOPIC 00111: Spectral Analysis VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_spectral_anls_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_spectral_anls_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Spectral Analysis VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Spectral Analysis VIs to perform array-based analysis on a spectrum.

| Palette Object | Description |
| --- | --- |
| Auto Power Spectrum | Computes the auto power spectrum of a time-domain signal X. For a real input signal, the power spectrum can be either single-sided or double-sided. For a complex input signal, the power spectrum is double-sided. |
| Cross Power | Computes the double-sided cross power spectrum of two time-domain signals X and Y. |
| Cross Power Spectrum | Computes the cross power spectrum of two time-domain signals X and Y. For real input signals, the cross power spectrum can be either single-sided or double-sided. For complex input signals, the cross power spectrum is double-sided. |
| Power Spectrum | Computes the double-sided power spectrum of a time-domain signal X. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_square.html language=enus -->
## TOPIC 00112: Square VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_square.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_square.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Square VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the square of elements in a sparse matrix.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Square Sparse Matrix (DBL)

[IMAGE alt='image' src='square_sparse_matrix__dbl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | A^2 returns a sparse matrix whose elements are the square elements in A. |

#### Square Sparse Matrix (SGL)

[IMAGE alt='image' src='square_sparse_matrix__sgl.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | A^2 returns a sparse matrix whose elements are the square elements in A. |

#### Square Sparse Matrix (CDB)

[IMAGE alt='image' src='square_sparse_matrix__cdb.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | A^2 returns a sparse matrix whose elements are the square elements in A. |

#### Square Sparse Matrix (CSG)

[IMAGE alt='image' src='square_sparse_matrix__csg.gif']

|  | A specifies the input sparse matrix. |
| --- | --- |
|  | A^2 returns a sparse matrix whose elements are the square elements in A. |

#### Square Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_subtract.html language=enus -->
## TOPIC 00113: Subtract VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_subtract.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_subtract.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Subtract VI

**Owning Palette:** [Numeric VIs](../lvmasmtref/masm_numeric_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the element-wise difference between two sparse matrices.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Subtract Sparse from Sparse (DBL)

[IMAGE alt='image' src='subtract_sparse_from_sparse__dbl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A-B returns the element-wise difference between A and B. |

#### Subtract Sparse from Sparse (SGL)

[IMAGE alt='image' src='subtract_sparse_from_sparse__sgl.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A-B returns the element-wise difference between A and B. |

#### Subtract Sparse from Sparse (CDB)

[IMAGE alt='image' src='subtract_sparse_from_sparse__cdb.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A-B returns the element-wise difference between A and B. |

#### Subtract Sparse from Sparse (CSG)

[IMAGE alt='image' src='subtract_sparse_from_sparse__csg.gif']

|  | A specifies the first sparse matrix. The number of rows and columns in A must be equal to the number of row and columns in B, respectively. |
| --- | --- |
|  | B specifies the second sparse matrix. The number of rows and columns in B must be equal to the number of row and columns in A, respectively. |
|  | A-B returns the element-wise difference between A and B. |

#### Subtract Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_sup_char.html language=enus -->
## TOPIC 00114: Support Characteristics for Multicore Analysis and Sparse Matrix VIs in Real-Time Applications (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_sup_char.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_sup_char.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Support Characteristics for Multicore Analysis and Sparse Matrix VIs in Real-Time Applications (Multicore Analysis and Sparse Matrix Toolkit)

The following sections define the support characteristics documented in the reference topic for each [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VI.

#### Supported on RT Targets

This category specifies if you can use the VI in an application you deploy to a real-time hardware target. VIs possess one of the following characteristic values:

- Yes —The VI is supported on RT targets.
- No —The VI is not supported on RT targets.

#### Suitable for Bounded Execution Times on RT

If the VI is supported on RT targets, this category specifies whether the VI typically executes in a bounded amount of time. VIs possess one of the following characteristic values:

- Yes —The VI is suitable for bounded execution times.
- Yes (with exceptions) —The VI is suitable for bounded execution times except under certain circumstances. When determinism in your application is important, avoid using these VIs under the circumstances specified in the help topic for each VI.
- No —The VI is supported on RT targets but it is known to cause unbounded execution times and increased jitter.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_support_rta.html language=enus -->
## TOPIC 00115: Support for Multicore Analysis and Sparse Matrix VIs in Real-Time Applications (Multicore Analysis and Sparse Matrix Toolkit)

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_support_rta.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_support_rta.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Support for Multicore Analysis and Sparse Matrix VIs in Real-Time Applications (Multicore Analysis and Sparse Matrix Toolkit)

You can deploy [Multicore Analysis and Sparse Matrix](../lvmasmtref/masm_vis.html) VIs to real-time (RT) targets. However, certain VIs are unsupported on RT targets. Also, although you can deploy certain VIs to RT targets, execution of those VIs at run time can cause increased jitter and unbounded execution times in the real-time application. Refer to the following lists for information about support for Multicore Analysis and Sparse Matrix VIs on RT targets.

#### VIs Not Supported on RT Targets

The following VIs are not supported on RT targets.

- Thread Management VIs
  - Get Number of Threads
  - Set Number of Threads
- Visualization VIs
  - Draw Sparse Graph
  - Draw Sparse Structure

#### VIs Suitable for Real-Time Applications

The following VIs execute in a bounded amount of time.

- Comparison VIs
  - Equal
  - Equal to Zero
  - Not Equal
- Linear Algebra VIs
  - A x B
  - Create Special Matrix
  - Dot Product
  - Generalized Eigenvalues and Vectors
  - Kronecker Product
  - Matrix Logarithm
  - Matrix Norm
  - Matrix Power
  - Matrix Rank
  - Matrix Square Root
  - Outer Product
  - PseudoInverse Matrix
  - QR Decomposition
  - QZ Decomposition
  - Schur Decomposition
  - SVD Decomposition
  - Trace
  - Transpose Matrix
  - Vector Norm
  - Sparse Linear Algebra VIs
    - Solve Triangular Equations
    - Trace
    - Transpose Matrix
- Matrix VIs
  - Get Matrix Size
  - Get Matrix Storage Format
  - Get Matrix Subset
  - Get Number of Nonzeros
  - Non-Conjugate Transpose Matrix
  - Reorder Elements
  - Set Matrix Size
  - Sparse to Dense
- Numeric VIs
  - Negate
  - Square
- Signal Operation VIs
  - Auto Correlation
  - Convolution
  - Cross Correlation
- Spectral Analysis VIs
  - Auto Power Spectrum
  - Cross Power
  - Cross Power Spectrum
  - Power Spectrum
- Transforms VIs
  - DCT
  - DST
  - FTT
  - Inverse DCT
  - Inverse DST
  - Inverse FFT
  - Inverse Multi-channel FFT
  - Multi-channel FFT

The following VIs typically execute in a bounded amount of time except under certain circumstances. When determinism in your application is important, avoid using these VIs under these circumstances. Refer to the *Details* section in each VI topic for more information about the exceptions.

- Linear Algebra VIs
  - Cholesky Decomposition
  - Determinant
  - Eigenvalues and Vectors
  - Inverse Matrix
  - LU Decomposition
  - Matrix Condition Number
  - Matrix Exponential
  - Solve Linear Equations
  - Sparse Linear Algebra VIs
    - A x B
- Numeric VIs
  - Absolute Value
  - Multiply
  - Complex VIs
    - Complex Conjugate
  - Conversion VIs
    - To Double Precision Complex
    - To Double Precision Float
    - To Double Precision Complex
    - To Double Precision Float

#### VIs That Cause Unbounded Execution Times in Real-Time Applications

The following VIs are supported on RT targets. However, these VIs are known to cause unbounded execution times and increased jitter. Avoid using these VIs when determinism in your application is important.

- File I/O VIs
  - Read from Matrix Market File
  - Write to Matrix Market File
- Linear Algebra VIs
  - Basic Linear Algebra Subroutines VIs
    - gemm – General Matrix–Matrix Product
    - gemv – General Matrix–Vector Product
    - hemm – Hermitian Matrix–Matrix Product
    - hemv – Hermitian Matrix–Vector Product
    - symm – Symmetric Matrix–Matrix Product
    - symv – Symmetric Matrix–Vector Product
    - trmm – Triangular Matrix–Matrix Product
    - trmm – Triangular Matrix–Vector Product
  - Sparse Linear Algebra VIs
    - Create Random Matrix
    - Create Special Matrix
    - PARDISO Advanced Cleaning Up
    - PARDISO Advanced Factorization
    - PARDISO Advanced Initialization
    - PARDISO Advanced Solver
    - PARDISO Solver
- Matrix VIs
  - Build Matrix
  - Concatenate Matrix
  - Create Matrix from Storage Format
  - Dense to Sparse
  - Initialize Matrix
  - Set Matrix Subset
  - Set Max Number of Nonzeros
- Numeric VIs
  - Add
  - Subtract
  - Complex VIs
    - Complex To Re Im
    - Re Im To Complex
- Visualization VIs
  - Draw Sparse Pattern

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_svd_decomposition.html language=enus -->
## TOPIC 00116: SVD Decomposition VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_svd_decomposition.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_svd_decomposition.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SVD Decomposition VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the singular value decomposition (SVD) of a matrix **A**.

Wire data to the **A** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### SVD Decomposition (DBL)

[IMAGE alt='image' src='svd_decomposition__dbl.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | singular values only? specifies whether to compute the singular values only. The default is FALSE. If singular values only? is TRUE, this VI does not compute Matrix U and Matrix V. |
|  | SVD option specifies how this VI performs the decomposition. 0Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and transpose of V (n × min(m,n)).1Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and transpose of V (n × n). |
| 0 | Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and transpose of V (n × min(m,n)). |
| 1 | Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and transpose of V (n × n). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector S returns the singular values of A in descending order. The values in Vector S are the diagonal elements of Matrix S. |
|  | Matrix U returns the decomposed U matrix. The columns of Matrix U compose an orthogonal set. Matrix U is empty if singular values only? is TRUE. |
|  | Matrix S returns the decomposed S matrix. Matrix S is a diagonal matrix whose diagonal elements are the values from Vector S, or the singular values of A in descending order. |
|  | Matrix V returns the decomposed V matrix. The columns of Matrix V compose an orthogonal set. Matrix V is empty if singular values only? is TRUE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SVD Decomposition (SGL)

[IMAGE alt='image' src='svd_decomposition__sgl.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | singular values only? specifies whether to compute the singular values only. The default is FALSE. If singular values only? is TRUE, this VI does not compute Matrix U and Matrix V. |
|  | SVD option specifies how this VI performs the decomposition. 0Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and transpose of V (n × min(m,n)).1Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and transpose of V (n × n). |
| 0 | Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and transpose of V (n × min(m,n)). |
| 1 | Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and transpose of V (n × n). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector S returns the singular values of A in descending order. The values in Vector S are the diagonal elements of Matrix S. |
|  | Matrix U returns the decomposed U matrix. The columns of Matrix U compose an orthogonal set. Matrix U is empty if singular values only? is TRUE. |
|  | Matrix S returns the decomposed S matrix. Matrix S is a diagonal matrix whose diagonal elements are the values from Vector S, or the singular values of A in descending order. |
|  | Matrix V returns the decomposed V matrix. The columns of Matrix V compose an orthogonal set. Matrix V is empty if singular values only? is TRUE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SVD Decomposition (CDB)

[IMAGE alt='image' src='svd_decomposition__cdb.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | singular values only? specifies whether to compute the singular values only. The default is FALSE. If singular values only? is TRUE, this VI does not compute Matrix U and Matrix V. |
|  | SVD option specifies how this VI performs the decomposition. 0Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and conjugated transpose of V (n × min(m,n)).1Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and conjugated transpose of V (n × n). |
| 0 | Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and conjugated transpose of V (n × min(m,n)). |
| 1 | Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and conjugated transpose of V (n × n). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector S returns the singular values of A in descending order. The values in Vector S are the diagonal elements of Matrix S. |
|  | Matrix U returns the decomposed U matrix. The columns of Matrix U compose an orthogonal set. Matrix U is empty if singular values only? is TRUE. |
|  | Matrix S returns the decomposed S matrix. Matrix S is a diagonal matrix whose diagonal elements are the values from Vector S, or the singular values of A in descending order. |
|  | Matrix V returns the decomposed V matrix. The columns of Matrix V compose an orthogonal set. Matrix V is empty if singular values only? is TRUE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SVD Decomposition (CSG)

[IMAGE alt='image' src='svd_decomposition__csg.gif']

|  | A specifies an m × n matrix with m rows and n columns. |
| --- | --- |
|  | singular values only? specifies whether to compute the singular values only. The default is FALSE. If singular values only? is TRUE, this VI does not compute Matrix U and Matrix V. |
|  | SVD option specifies how this VI performs the decomposition. 0Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and conjugated transpose of V (n × min(m,n)).1Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and conjugated transpose of V (n × n). |
| 0 | Thin (default)—Decomposes an m × n matrix A as the multiplication of matrix U (m × min(m,n)), S (min(m,n) × min(m,n)), and conjugated transpose of V (n × min(m,n)). |
| 1 | Full—Decomposes an m × n matrix A as the multiplication of matrix U (m × m), S (m × n), and conjugated transpose of V (n × n). |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Vector S returns the singular values of A in descending order. The values in Vector S are the diagonal elements of Matrix S. |
|  | Matrix U returns the decomposed U matrix. The columns of Matrix U compose an orthogonal set. Matrix U is empty if singular values only? is TRUE. |
|  | Matrix S returns the decomposed S matrix. Matrix S is a diagonal matrix whose diagonal elements are the values from Vector S, or the singular values of A in descending order. |
|  | Matrix V returns the decomposed V matrix. The columns of Matrix V compose an orthogonal set. Matrix V is empty if singular values only? is TRUE. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SVD Decomposition Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

Refer to the [Details](/csh?topicname=gmath/svd_decomp.html) section in the [SVD Decomposition](/csh?topicname=gmath/svd_decomp.html) VI for more details about this VI.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_symm.html language=enus -->
## TOPIC 00117: symm - Symmetric Matrix-Matrix Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_symm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_symm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### symm - Symmetric Matrix-Matrix Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a symmetric matrix and another matrix.

Wire data to the **A**, **B**, and **C** inputs to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### dsymm - Symmetric Matrix-Matrix Product (DBL)

[IMAGE alt='image' src='dsymm_-_symmetric_matrix-matrix_product__dbl.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a symmetric matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by B. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*A or A*B. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | dsymm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the result of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### ssymm - Symmetric Matrix-Matrix Product (SGL)

[IMAGE alt='image' src='ssymm_-_symmetric_matrix-matrix_product__sgl.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a symmetric matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by b. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to zero. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*A or A*B. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | ssymm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the result of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### zsymm - Symmetric Matrix-Matrix Product (CDB)

[IMAGE alt='image' src='zsymm_-_symmetric_matrix-matrix_product__cdb.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a symmetric matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by b. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*A or A*B. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | zsymm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the result of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### csymm - Symmetric Matrix-Matrix Product (CSG)

[IMAGE alt='image' src='csymm_-_symmetric_matrix-matrix_product__csg.gif']

|  | side A specifies the position of A in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*A + beta*C.1Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*A + beta*C. |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*A*B+beta*C. |
|  | A specifies a symmetric matrix. This VI multiplies the first K rows and K columns of the triangular component of A that you select for matrix A type by b. If you set side A to Left, K equals the number of rows in B. If you set side A to Right, K equals the number of columns in B. A must have at least K rows and K columns. |
|  | B specifies a matrix. |
|  | C specifies a matrix of dimensions greater than or equal to the dimensions of B. The default is a matrix of the same size as B with all elements equal to zero. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*A or A*B. The default is 1. |
|  | beta specifies a scalar that scales C. The default is 1. |
|  | csymm returns a matrix of the same size as C. For elements of the first K rows and K columns, this VI returns the result of alpha*B*A + beta*C or alpha*A*B + beta*C. For any remaining elements, this VI returns the value of the element in C with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### symm - Symmetric Matrix-Matrix Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_symv.html language=enus -->
## TOPIC 00118: symv - Symmetric Matrix-Vector Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_symv.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_symv.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### symv - Symmetric Matrix-Vector Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a symmetric matrix and a vector.

Wire data to the **A**, **x**, and **y** inputs to determine the polymorphic instance to use.

[Details](#details)

#### dsymv - Symmetric Matrix-Vector Product (DBL)

[IMAGE alt='image' src='dsymv_-_symmetric_matrix-vector_product__dbl.gif']

|  | A specifies a symmetric matrix. This VI multiplies the first N rows and N columns of the triangular component of A that you select for matrix A type by x, where N is the number of elements in x. A must have at least N rows and N columns. |
| --- | --- |
|  | x specifies a vector with N elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to 0. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | dsymv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*A*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### ssymv - Symmetric Matrix-Vector Product (SGL)

[IMAGE alt='image' src='ssymv_-_symmetric_matrix-vector_product__sgl.gif']

|  | A specifies a symmetric matrix. This VI multiplies the first N rows and N columns of the triangular component of A that you select for matrix A type by x, where N is the number of elements in x. A must have at least N rows and N columns. |
| --- | --- |
|  | x specifies a vector with N elements. |
|  | y specifies a vector. y must have at least N elements. The default is an N-element vector with all elements equal to zero. |
|  | matrix A type specifies whether this VI uses the upper or lower triangular matrix component of A to calculate the product. 2Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A.3Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
| 2 | Lower Triangular—Specifies that this VI uses the lower triangular matrix component of A. |
| 3 | Upper Triangular (default)—Specifies that this VI uses the upper triangular matrix component of A. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales A*x. The default is 1. |
|  | beta specifies a scalar that scales y. The default is 1. |
|  | ssymv returns a vector of the same size as y. For the first N elements, this VI returns the results of alpha*A*x + beta*y. For any remaining elements, this VI returns the value of the element in y with the same index. |
|  | error out contains error information. This output provides standard error out functionality. |

#### symv - Symmetric Matrix-Vector Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_thread_mgmt.html language=enus -->
## TOPIC 00119: Thread Management VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_thread_mgmt.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_thread_mgmt.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Thread Management VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Thread Management VIs to manage the maximum number of threads in parallelism.

| Palette Object | Description |
| --- | --- |
| Get Number of Threads | Gets the maximum number of threads available for parallelism. |
| Set Number of Threads | Sets the maximum number of threads for parallelism. LabVIEW does not guarantee that the number of threads you set is used in calculations. The actual number of threads that LabVIEW uses depends on the problem size, system resources, and other considerations. By default, the Multicore Analysis and Sparse Matrix VIs use the number of physical cores as the maximum number of threads unless you specify a smaller number. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_to_dbl_prec_complex.html language=enus -->
## TOPIC 00120: To Double Precision Complex VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_to_dbl_prec_complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_to_dbl_prec_complex.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### To Double Precision Complex VI

**Owning Palette:** [Conversion VIs](../lvmasmtref/masm_conversion_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts elements in a sparse matrix to double-precision, complex numbers.

If the input sparse matrix is a real matrix, LabVIEW sets the imaginary parts of the elements to zero in the output sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### To CDB Sparse Matrix (DBL)

[IMAGE alt='image' src='to_cdb_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CDB Sparse Matrix returns a complex, double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, complex numbers. |

#### To CDB Sparse Matrix (SGL)

[IMAGE alt='image' src='to_cdb_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CDB Sparse Matrix returns a complex, double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, complex numbers. |

#### To CDB Sparse Matrix (CDB)

[IMAGE alt='image' src='to_cdb_sparse_matrix__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CDB Sparse Matrix returns a complex, double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, complex numbers. |

#### To CDB Sparse Matrix (CSG)

[IMAGE alt='image' src='to_cdb_sparse_matrix__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CDB Sparse Matrix returns a complex, double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, complex numbers. |

#### To Double Precision Complex Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: To CDB Sparse Matrix (DBL) To CDB Sparse Matrix (SGL) To CDB Sparse Matrix (CSG) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_to_dbl_prec_float.html language=enus -->
## TOPIC 00121: To Double Precision Float VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_to_dbl_prec_float.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_to_dbl_prec_float.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### To Double Precision Float VI

**Owning Palette:** [Conversion VIs](../lvmasmtref/masm_conversion_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts elements in a sparse matrix to double-precision, floating-point numbers.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### To DBL Sparse Matrix (DBL)

[IMAGE alt='image' src='to_dbl_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies a real sparse matrix. |
| --- | --- |
|  | DBL Sparse Matrix returns a double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, floating-point numbers. |

#### To DBL Sparse Matrix (SGL)

[IMAGE alt='image' src='to_dbl_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies a real sparse matrix. |
| --- | --- |
|  | DBL Sparse Matrix returns a double sparse matrix whose elements are elements in the Sparse Matrix and converted to double-precision, floating-point numbers. |

#### To Double Precision Float Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instance is an exception: To DBL Sparse Matrix (SGL) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_to_sgl_prec_complex.html language=enus -->
## TOPIC 00122: To Single Precision Complex VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_to_sgl_prec_complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_to_sgl_prec_complex.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### To Single Precision Complex VI

**Owning Palette:** [Conversion VIs](../lvmasmtref/masm_conversion_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts elements in a sparse matrix to single-precision, complex numbers.

If the input sparse matrix is a real matrix, LabVIEW sets the imaginary part of the elements to zero in the output sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### To CSG Sparse Matrix (DBL)

[IMAGE alt='image' src='to_csg_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CSG Sparse Matrix returns a complex, single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, complex numbers. |

#### To CSG Sparse Matrix (SGL)

[IMAGE alt='image' src='to_csg_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CSG Sparse Matrix returns a complex, single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, complex numbers. |

#### To CSG Sparse Matrix (CDB)

[IMAGE alt='image' src='to_csg_sparse_matrix__cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CSG Sparse Matrix returns a complex, single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, complex numbers. |

#### To CSG Sparse Matrix (CSG)

[IMAGE alt='image' src='to_csg_sparse_matrix__csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. |
| --- | --- |
|  | CSG Sparse Matrix returns a complex, single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, complex numbers. |

#### To Single Precision Complex Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instances are exceptions: To CSG Sparse Matrix (DBL) To CSG Sparse Matrix (SGL) To CSG Sparse Matrix (CDB) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_to_sgl_prec_float.html language=enus -->
## TOPIC 00123: To Single Precision Float VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_to_sgl_prec_float.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_to_sgl_prec_float.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### To Single Precision Float VI

**Owning Palette:** [Conversion VIs](../lvmasmtref/masm_conversion_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Converts elements in a sparse matrix to single-precision, floating-point numbers.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### To SGL Sparse Matrix (DBL)

[IMAGE alt='image' src='to_sgl_sparse_matrix__dbl.gif']

|  | Sparse Matrix specifies a real sparse matrix. |
| --- | --- |
|  | SGL Sparse Matrix returns a single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, floating-point numbers. |

#### To SGL Sparse Matrix (SGL)

[IMAGE alt='image' src='to_sgl_sparse_matrix__sgl.gif']

|  | Sparse Matrix specifies a real sparse matrix. |
| --- | --- |
|  | SGL Sparse Matrix returns a single sparse matrix whose elements are elements in the Sparse Matrix and converted to single-precision, floating-point numbers. |

#### To Single Precision Float Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes (with exceptions). The following instance is an exception: To SGL Sparse Matrix (DBL) |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_trace.html language=enus -->
## TOPIC 00124: Trace VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_trace.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_trace.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Trace VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the trace of a sparse matrix.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Trace (DBL)

[IMAGE alt='image' src='trace_sparse_dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal in Sparse Matrix. If any error occurs, trace returns NaN. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (SGL)

[IMAGE alt='image' src='trace_sparse_sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal in Sparse Matrix. If any error occurs, trace returns NaN. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (CDB)

[IMAGE alt='image' src='trace_sparse_cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal in Sparse Matrix. If any error occurs, trace returns NaN + NaNi. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace (CSG)

[IMAGE alt='image' src='trace_sparse_csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trace returns the sum of the main diagonal in Sparse Matrix. If any error occurs, trace returns NaN + NaNi. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Trace Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_transforms_vis.html language=enus -->
## TOPIC 00125: Transforms VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_transforms_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_transforms_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Transforms VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Transforms VIs to implement common transforms used in signal processing.

| Palette Object | Description |
| --- | --- |
| DCT | Computes the Discrete Cosine Transform (DCT) of the input sequence X. |
| DST | Computes the Discrete Sine Transform (DST) of the input sequence X. |
| FFT | Computes the fast Fourier transform (FFT) of the input sequence X. |
| Inverse DCT | Computes the inverse Discrete Cosine Transform (DCT) of the input sequence DCT {X}. |
| Inverse DST | Computes the inverse Discrete Sine Transform (DST) of the input sequence DST {X}. |
| Inverse FFT | Computes the inverse fast Fourier transform (FFT) of the input sequence X. |
| Inverse Multi-channel FFT | Computes the inverse fast Fourier transform (IFFT) of the frequency-domain sequence in each channel in Multi-channel FFT {X}. |
| Multi-channel FFT | Computes the fast Fourier transform (FFT) of each channel signal of the input matrix X. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_transpose.html language=enus -->
## TOPIC 00126: Transpose Matrix VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_transpose.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_transpose.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Transpose Matrix VI

**Owning Palette:** [Sparse Linear Algebra VIs](../lvmasmtref/masm_sparse_lin_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Transposes a sparse matrix. If the matrix is a complex sparse matrix, this VI performs conjugate transposition.

Wire data to the **Sparse Matrix** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Transpose Matrix (DBL)

[IMAGE alt='image' src='transpose_matrix_sparse_dbl.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Transposed Sparse Matrix returns the transpose of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (SGL)

[IMAGE alt='image' src='transpose_matrix_sparse_sgl.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Transposed Sparse Matrix returns the transpose of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (CDB)

[IMAGE alt='image' src='transpose_matrix_sparse_cdb.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Transposed Sparse Matrix returns the conjugate transpose of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix (CSG)

[IMAGE alt='image' src='transpose_matrix_sparse_csg.gif']

|  | Sparse Matrix specifies the input sparse matrix. Sparse Matrix must not be empty. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Transposed Sparse Matrix returns the conjugate transpose of Sparse Matrix. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Transpose Matrix Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_trmm.html language=enus -->
## TOPIC 00127: trmm - Triangular Matrix-Matrix Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_trmm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_trmm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### trmm - Triangular Matrix-Matrix Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a triangular matrix and another matrix.

Wire data to the **A** and **B** inputs to determine the polymorphic instance to use.

[Details](#details)

#### dtrmm - Triangular Matrix-Matrix Product (DBL)

[IMAGE alt='image' src='dtrmm_-_triangular_matrix-matrix_product__dbl.gif']

|  | side A specifies the position of op(A) in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*op(A).1Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*op(A). |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first K rows and K columns of op(A) by B. If you set side A to Left, K equals the number of row in B. If you set side A to Right, K equals the number of columns in B. A must have at least K row and K columns. |
|  | B specifies a matrix. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*op(A) or op(A)*B. The default is 1. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | dtrmm is a matrix of the same size as B that returns the result of alpha*op(A)*B or alpha*B*op(A). |
|  | error out contains error information. This output provides standard error out functionality. |

#### strmm - Triangular Matrix-Matrix Product (SGL)

[IMAGE alt='image' src='strmm_-_triangular_matrix-matrix_product__sgl.gif']

|  | side A specifies the position of op(A) in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*op(A).1Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*op(A). |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first K rows and K columns of op(A) by B. If you set side A to Left, K equals the number of row in B. If you set side A to Right, K equals the number of columns in B. A must have at least K row and K columns. |
|  | B specifies a matrix. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*op(A) or op(A)*B. The default is 1. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | strmm is a matrix of the same size as B that returns the result of alpha*op(A)*B or alpha*B*op(A). |
|  | error out contains error information. This output provides standard error out functionality. |

#### ztrmm - Triangular Matrix-Matrix Product (CDB)

[IMAGE alt='image' src='ztrmm_-_triangular_matrix-matrix_product__cdb.gif']

|  | side A specifies the position of op(A) in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*op(A).1Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*op(A). |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first K rows and K columns of op(A) by B. If you set side A to Left, K equals the number of row in B. If you set side A to Right, K equals the number of columns in B. A must have at least K row and K columns. |
|  | B specifies a matrix. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*op(A) or op(A)*B. The default is 1. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | ztrmm is a matrix of the same size as B that returns the result of alpha*op(A)*B or alpha*B*op(A). |
|  | error out contains error information. This output provides standard error out functionality. |

#### ctrmm - Triangular Matrix-Matrix Product (CSG)

[IMAGE alt='image' src='ctrmm_-_triangular_matrix-matrix_product__csg.gif']

|  | side A specifies the position of op(A) in the calculation. 0Right—Specifies that this VI calculates the result of alpha*B*op(A).1Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
| --- | --- |
| 0 | Right—Specifies that this VI calculates the result of alpha*B*op(A). |
| 1 | Left (default)—Specifies that this VI calculates the result of alpha*op(A)*B. |
|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first K rows and K columns of op(A) by B. If you set side A to Left, K equals the number of row in B. If you set side A to Right, K equals the number of columns in B. A must have at least K row and K columns. |
|  | B specifies a matrix. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | alpha specifies a scalar that scales B*op(A) or op(A)*B. The default is 1. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | ctrmm is a matrix of the same size as B that returns the result of alpha*op(A)*B or alpha*B*op(A). |
|  | error out contains error information. This output provides standard error out functionality. |

#### trmm - Triangular Matrix-Matrix Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_trmv.html language=enus -->
## TOPIC 00128: trmv - Triangular Matrix-Vector Product VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_trmv.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_trmv.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### trmv - Triangular Matrix-Vector Product VI

**Owning Palette:** [Basic Linear Algebra Subroutines VIs](../lvmasmtref/masm_blas_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Calculates the product of a triangular matrix and a vector.

Wire data to the **A** and **x** inputs to determine the polymorphic instance to use.

[Details](#details)

#### dtrmv - Triangular Matrix-Vector Product (DBL)

[IMAGE alt='image' src='dtrmv_-_triangular_matrix-vector_product__dbl.gif']

|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first N rows and N columns of op(A) by x, where N is the number of elements in x. op(A) must have at least N rows and N columns. |
|  | x specifies a vector with N elements. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | dtrmv returns a vector of the same size as x that returns the result of op(A)*x. |
|  | error out contains error information. This output provides standard error out functionality. |

#### strmv - Triangular Matrix-Vector Product (SGL)

[IMAGE alt='image' src='strmv_-_triangular_matrix-vector_product__sgl.gif']

|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first N rows and N columns of op(A) by x, where N is the number of elements in x. op(A) must have at least N rows and N columns. |
|  | x specifies a vector with N elements. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | strmv returns a vector of the same size as x that returns the result of op(A)*x. |
|  | error out contains error information. This output provides standard error out functionality. |

#### ztrmv - Triangular Matrix-Vector Product (CDB)

[IMAGE alt='image' src='ztrmv_-_triangular_matrix-vector_product__cdb.gif']

|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first N rows and N columns of op(A) by x, where N is the number of elements in x. op(A) must have at least N rows and N columns. |
|  | x specifies a vector with N elements. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | ztrmv returns a vector of the same size as x that returns the result of op(A)*x. |
|  | error out contains error information. This output provides standard error out functionality. |

#### ctrmv - Triangular Matrix-Vector Product (CSG)

[IMAGE alt='image' src='ctrmv_-_triangular_matrix-vector_product__csg.gif']

|  | operation A specifies the operation to perform on matrix A that results in matrix op(A). 0Direct (default)1Conjugated & Transposed2Transposed |
| --- | --- |
| 0 | Direct (default) |
| 1 | Conjugated & Transposed |
| 2 | Transposed |
|  | A specifies a triangular matrix. This VI multiplies the first N rows and N columns of op(A) by x, where N is the number of elements in x. op(A) must have at least N rows and N columns. |
|  | x specifies a vector with N elements. |
|  | matrix A type specifies whether A is an upper or lower triangular matrix. 2Lower Triangular—Specifies that A is a lower triangular matrix.3Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
| 2 | Lower Triangular—Specifies that A is a lower triangular matrix. |
| 3 | Upper Triangular (default)—Specifies that A is an upper triangular matrix. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | diagonal A specifies the value of the diagonal elements of A. 0Non-unit (default)—Specifies that this VI uses the original diagonal elements of A1Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
| 0 | Non-unit (default)—Specifies that this VI uses the original diagonal elements of A |
| 1 | Unit—Specifies that this VI uses the value of 1 for all diagonal elements of A. |
|  | ctrmv returns a vector of the same size as x that returns the result of op(A)*x. |
|  | error out contains error information. This output provides standard error out functionality. |

#### trmv - Triangular Matrix-Vector Product Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_vector_norm.html language=enus -->
## TOPIC 00129: Vector Norm VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_vector_norm.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_vector_norm.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Vector Norm VI

**Owning Palette:** [Linear Algebra VIs](../lvmasmtref/masm_linear_algebra_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Computes the norm of **Input Vector**.

Wire data to the **Input Vector** input to determine the polymorphic instance to use or [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the instance.

[Details](#details)

#### Vector Norm (DBL)

[IMAGE alt='image' src='vector_norm__dbl.gif']

|  | Input Vector specifies a vector. If Input Vector is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of vector norm to compute. Let X represent the Input Vector. \|\|X\|\|p represents the norm of X, where p are the different types of vector norms, such as 1-norm, 2-norm, and so on, that this VI can compute. 11-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\|22-norm (default)—Specifies that the norm of X is defined by the following:3Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|)4-Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|)5User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
| 1 | 1-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\| |
| 2 | 2-norm (default)—Specifies that the norm of X is defined by the following: |
| 3 | Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|) |
| 4 | -Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|) |
| 5 | User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
|  | user defined norm specifies the user defined norm type. The default is –1. user defined norm is valid only if norm type is User Defined. user defined norm must be nonzero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector Norm (SGL)

[IMAGE alt='image' src='vector_norm__sgl.gif']

|  | Input Vector specifies a vector. If Input Vector is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of vector norm to compute. Let X represent the Input Vector. \|\|X\|\|p represents the norm of X, where p are the different types of vector norms, such as 1-norm, 2-norm, and so on, that this VI can compute. 11-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\|22-norm (default)—Specifies that the norm of X is defined by the following:3Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|)4-Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|)5User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
| 1 | 1-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\| |
| 2 | 2-norm (default)—Specifies that the norm of X is defined by the following: |
| 3 | Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|) |
| 4 | -Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|) |
| 5 | User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
|  | user defined norm specifies the user defined norm type. The default is –1. user defined norm is valid only if norm type is User Defined. user defined norm must be nonzero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector Norm (CDB)

[IMAGE alt='image' src='vector_norm__cdb.gif']

|  | Input Vector specifies a vector. If Input Vector is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of vector norm to compute. Let X represent the Input Vector. \|\|X\|\|p represents the norm of X, where p are the different types of vector norms, such as 1-norm, 2-norm, and so on, that this VI can compute. 11-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\|22-norm (default)—Specifies that the norm of X is defined by the following:3Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|)4-Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|)5User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
| 1 | 1-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\| |
| 2 | 2-norm (default)—Specifies that the norm of X is defined by the following: |
| 3 | Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|) |
| 4 | -Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|) |
| 5 | User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
|  | user defined norm specifies the user defined norm type. The default is –1. user defined norm is valid only if norm type is User Defined. user defined norm must be nonzero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector Norm (CSG)

[IMAGE alt='image' src='vector_norm__csg.gif']

|  | Input Vector specifies a vector. If Input Vector is empty, this VI sets norm to NaN. |
| --- | --- |
|  | norm type specifies the type of vector norm to compute. Let X represent the Input Vector. \|\|X\|\|p represents the norm of X, where p are the different types of vector norms, such as 1-norm, 2-norm, and so on, that this VI can compute. 11-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\|22-norm (default)—Specifies that the norm of X is defined by the following:3Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|)4-Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|)5User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
| 1 | 1-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|1=\|x0\|+\|x1\|+…+\|xn-1\| |
| 2 | 2-norm (default)—Specifies that the norm of X is defined by the following: |
| 3 | Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|Inf=maxi(\|xi\|) |
| 4 | -Inf-norm—Specifies that the norm of X is defined by the following:\|\|X\|\|-Inf=mini(\|xi\|) |
| 5 | User Defined—Specifies that the norm of X is defined by the following:where y is user defined norm. |
|  | user defined norm specifies the user defined norm type. The default is –1. user defined norm is valid only if norm type is User Defined. user defined norm must be nonzero. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | norm returns the norm of Input Vector. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Vector Norm Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | Yes |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_vis.html language=enus -->
## TOPIC 00130: Multicore Analysis and Sparse Matrix VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Multicore Analysis and Sparse Matrix VIs

June 2012, 373601B-01

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Multicore Analysis and Sparse Matrix VIs to compute performance-sensitive mathematical and signal processing functions.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Multicore Analysis and Sparse Matrix error codes](../lvmasmtref/lvmasmt_error_codes.html).

| Subpalette | Description |
| --- | --- |
| Comparison VIs | Use the Comparison VIs to compare sparse matrices. |
| File I/O VIs | Use the File I/O VIs to read from and write to a file in the Matrix Market exchange format. |
| Linear Algebra VIs | Use the Linear Algebra VIs to perform matrix-related computations and analysis. |
| Matrix VIs | Use the Matrix VIs to manipulate the elements, diagonals, and submatrices of a sparse matrix. |
| Numeric VIs | Use the Numeric VIs to create and perform arithmetic and complex mathematical operations on sparse matrices and to convert sparse matrices from one data type to another. |
| Signal Operation VIs | Use the Signal Operation VIs to manipulate signals and return a signal output. |
| Spectral Analysis VIs | Use the Spectral Analysis VIs to perform array-based analysis on a spectrum. |
| Thread Management VIs | Use the Thread Management VIs to manage the maximum number of threads in parallelism. |
| Transforms VIs | Use the Transforms VIs to implement common transforms used in signal processing. |
| Visualization VIs | Use the Visualization VIs to render sparse matrices in different views. |

© 2011–2012 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_visualization_vis.html language=enus -->
## TOPIC 00131: Visualization VIs

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_visualization_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_visualization_vis.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Visualization VIs

**Owning Palette:** [Multicore Analysis and Sparse Matrix VIs](../lvmasmtref/masm_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Visualization VIs to render sparse matrices in different views.

| Palette Object | Description |
| --- | --- |
| Draw Sparse Graph | Treats the sparse matrix as an adjacency matrix and draws the graph. |
| Draw Sparse Pattern | Draws the pattern of elements in a sparse matrix. The pattern shows the coordinates, the row and column indices, of elements in the sparse matrix. This VI ignores the actual values of elements in the sparse matrix. |
| Draw Sparse Structure | Draws the structure of elements in a sparse matrix. The structure shows not only the coordinates, the row and column indices, of elements, but also the actual values of elements in the sparse matrix. |

<!--NI_TOPIC bundle=labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref path=lvmasmtref/masm_write_to_matrix_mkt.html language=enus -->
## TOPIC 00132: Write to Matrix Market File VI

- bundle_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- source_path: `lvmasmtref/masm_write_to_matrix_mkt.html`
- source_url: https://docs-be.ni.com/bundle/labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref/raw/resource/enus/lvmasmtref/masm_write_to_matrix_mkt.html
- document_id: `labview-multicore-analysis-and-sparse-matrix-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Write to Matrix Market File VI

**Owning Palette:** [File I/O VIs](../lvmasmtref/masm_file_vis.html)

**Requires:** Multicore Analysis and Sparse Matrix Toolkit

Writes a matrix into a file in the Matrix Market exchange format.

You must [manually select](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) the polymorphic instance you want to use.

[Details](#details)  [Example](#examples)

#### Write Sparse to Matrix Market (DBL)

[IMAGE alt='image' src='write_sparse_to_matrix_market__dbl.gif']

|  | pattern only? specifies whether to write sparsity pattern, the row indices and column indices of elements, into Matrix Market file. The default is to write both pattern and elements. |
| --- | --- |
|  | Matrix Market file specifies an absolute path to a file into which you want to write the matrix. The file can be a new file or an existing file. If the file exists, you must confirm whether to overwrite the existing file. |
|  | Sparse Matrix specifies the matrix to write into Matrix Market file. This input must be a square matrix if matrix type is Symmetric, Skew-symmetric, or Hermitian. |
|  | matrix type specifies the matrix type and how to write matrix elements into Matrix Market file. 0General (default)—The matrix is a general matrix. All elements write into the file.1Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file.3Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
| 0 | General (default)—The matrix is a general matrix. All elements write into the file. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | description specifies the description of the matrix to write into Matrix Market file. |
|  | Matrix Market file out returns Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write Sparse to Matrix Market (CDB)

[IMAGE alt='image' src='write_sparse_to_matrix_market__cdb.gif']

|  | pattern only? specifies whether to write sparsity pattern, the row indices and column indices of elements, into Matrix Market file. The default is to write both pattern and elements. |
| --- | --- |
|  | Matrix Market file specifies an absolute path to a file into which you want to write the matrix. The file can be a new file or an existing file. If the file exists, you must confirm whether to overwrite the existing file. |
|  | Sparse Matrix specifies the matrix to write into Matrix Market file. This input must be a square matrix if matrix type is Symmetric, Skew-symmetric, or Hermitian. |
|  | matrix type specifies the matrix type and how to write matrix elements into Matrix Market file. 0General (default)—The matrix is a general matrix. All elements write into the file.1Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file.3Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
| 0 | General (default)—The matrix is a general matrix. All elements write into the file. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | description specifies the description of the matrix to write into Matrix Market file. |
|  | Matrix Market file out returns Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write Dense to Matrix Market (DBL)

[IMAGE alt='image' src='write_dense_to_matrix_market__dbl.gif']

|  | Matrix Market file specifies an absolute path to a file into which you want to write the matrix. The file can be a new file or an existing file. If the file exists, you must confirm whether to overwrite the existing file. |
| --- | --- |
|  | Dense Matrix specifies the matrix to write into Matrix Market file. This input must be a square matrix if matrix type is Symmetric, Skew-symmetric, or Hermitian. |
|  | matrix type specifies the matrix type and how to write matrix elements into Matrix Market file. 0General (default)—The matrix is a general matrix. All elements write into the file.1Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file.3Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
| 0 | General (default)—The matrix is a general matrix. All elements write into the file. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | description specifies the description of the matrix to write into Matrix Market file. |
|  | Matrix Market file out returns Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write Dense to Matrix Market (CDB)

[IMAGE alt='image' src='write_dense_to_matrix_market__cdb.gif']

|  | Matrix Market file specifies an absolute path to a file into which you want to write the matrix. The file can be a new file or an existing file. If the file exists, you must confirm whether to overwrite the existing file. |
| --- | --- |
|  | Dense Matrix specifies the matrix to write into Matrix Market file. This input must be a square matrix if matrix type is Symmetric, Skew-symmetric, or Hermitian. |
|  | matrix type specifies the matrix type and how to write matrix elements into Matrix Market file. 0General (default)—The matrix is a general matrix. All elements write into the file.1Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file.2Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file.3Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
| 0 | General (default)—The matrix is a general matrix. All elements write into the file. |
| 1 | Symmetric—The matrix is a symmetric matrix. Only elements in the lower triangular part of the matrix write into the file. |
| 2 | Skew-symmetric—The matrix is a skew-symmetric matrix. Only elements in the strict lower triangular part of the matrix write into the file. |
| 3 | Hermitian—The matrix is a Hermitian matrix. Only elements in the lower triangular part write into the file. This matrix type applies only to complex matrices. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | description specifies the description of the matrix to write into Matrix Market file. |
|  | Matrix Market file out returns Matrix Market file. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write to Matrix Market File Details

The following table lists the [support characteristics](../lvmasmtref/masm_sup_char.html) of this VI.

| Supported on RT targets | Yes |
| --- | --- |
| Suitable for bounded execution times on RT | No |

#### Example

Refer to the Write Matrix to Matrix Market File VI in the labview\examples\Multicore Analysis and Sparse Matrix\Sparse Matrix directory for an example of using the Write to Matrix Market File VI.
