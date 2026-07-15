# NI OSS SOURCE SNAPSHOT: grpc-teststand-api

<!--NI_OSS_SNAPSHOT repo=ni/grpc-teststand-api commit=bffa744c44dfcd45847898da813104855f2401c4 -->

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/AssemblyInfo.cs sha256=4930dddfc8fc272febb229167f0fc173621817aa44d765653ae093804d1b2b10 bytes=2658 -->
## FILE: Server/UI/AssemblyInfo.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/AssemblyInfo.cs`
- sha256: `4930dddfc8fc272febb229167f0fc173621817aa44d765653ae093804d1b2b10`
- bytes: 2658

````csharp
using System.Reflection;
using NationalInstruments.TestStand.Interop.API;

//
// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
//
[assembly: AssemblyTitle(VersionConstants.VersionConstant_Product + " Simple CSharp User Interface")]
[assembly: AssemblyDescription(VersionConstants.VersionConstant_Product + " Simple CSharp User Interface")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("[YourCompanyHere]")]
[assembly: AssemblyProduct("[YourProductNameHere]")]
[assembly: AssemblyCopyright("[YourCopyrightHere]")]
[assembly: AssemblyTrademark("[YourTrademarkHere]")]
[assembly: AssemblyCulture("")]		

//
// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Revision and Build Numbers 
// by using the '*' as shown below:

[assembly: AssemblyVersion("1.0.0.0")]

//
// In order to sign your assembly you must specify a key to use. Refer to the 
// Microsoft .NET Framework documentation for more information on assembly signing.
//
// Use the attributes below to control which key is used for signing. 
//
// Notes: 
//   (*) If no key is specified, the assembly is not signed.
//   (*) KeyName refers to a key that has been installed in the Crypto Service
//       Provider (CSP) on your machine. KeyFile refers to a file which contains
//       a key.
//   (*) If the KeyFile and the KeyName values are both specified, the 
//       following processing occurs:
//       (1) If the KeyName can be found in the CSP, that key is used.
//       (2) If the KeyName does not exist and the KeyFile does exist, the key 
//           in the KeyFile is installed into the CSP and used.
//   (*) In order to create a KeyFile, you can use the sn.exe (Strong Name) utility.
//       When specifying the KeyFile, the location of the KeyFile should be
//       relative to the project output directory which is
//       %Project Directory%\obj\<configuration>. For example, if your KeyFile is
//       located in the project directory, you would specify the AssemblyKeyFile 
//       attribute as [assembly: AssemblyKeyFile("..\\..\\mykey.snk")]
//   (*) Delay Signing is an advanced option - see the Microsoft .NET Framework
//       documentation for more information on this.
//
[assembly: AssemblyDelaySign(false)]
[assembly: AssemblyKeyFile("")]
[assembly: AssemblyKeyName("")]
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/GrpcServer.cs sha256=e4c8a5a4c799ec80e09c08aedb5222972676d0443a6ce3e6ae274c9d4f596651 bytes=1143 -->
## FILE: Server/UI/GrpcServer.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/GrpcServer.cs`
- sha256: `e4c8a5a4c799ec80e09c08aedb5222972676d0443a6ce3e6ae274c9d4f596651`
- bytes: 1143

````csharp
using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using TestStandGrpcApi;

namespace TestExecServer
{
	internal class GrpcServer : GrpcServerBase
	{
		public static event EventHandler<Exception> StartupException;

        public static void Start(string[] args)
		{
			InitializeServerOptions(args);

			ServerHost = CreateHostBuilder<GrpcServer>(args).Build();
			Task.Run(() =>
			{ 
				try
				{
					ServerHost.Run();
				}
				catch (Exception exception)
				{
					StartupException?.Invoke(null, exception);
                }
			});
		}

		public GrpcServer(IConfiguration configuration) : base(configuration)
		{
		}

		public static void ConfigureServices(IServiceCollection services)
		{
			ConfigureServicesCore(services);
		}

		public static void Configure(IApplicationBuilder app, IWebHostEnvironment webHostEnvironment)
		{
            ConfigureCore(app, webHostEnvironment);
		}
	}
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/MainForm.cs sha256=b9b58e7aa5cb61e48df896210b41dcf99f0abdbaa15f9ed82a5decf396dd56a8 bytes=45188 -->
## FILE: Server/UI/MainForm.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/MainForm.cs`
- sha256: `b9b58e7aa5cb61e48df896210b41dcf99f0abdbaa15f9ed82a5decf396dd56a8`
- bytes: 45188

````csharp
// Note:	This application has a manifest file in the project. This manifest file includes the Microsoft.Windows.Common-Controls which 
//			enables the application to display controls using the XP theme that the operating system selects.
//			A post build event embeds this manifest file into the executable.
//			In order for the manifest file to enable the executable to display with the XP theme:
//			1. The manifest file must have the same name as the executable. For example, if your executable is named MyExecutable.exe, your manifest file is required to have the name MyExecutable.exe.manifest.
//			2. The manifest file must include the Microsoft.Windows.Common-Controls.
//			3. The manifest file must reside in the same directory as the executable.
//			Also note that if you enable the Project Properties>>Debug>>Enable Visual Studio Hosting Process option, the XP theme adaption does not occur when debugging the executable
//			because the Visual Studio environment creates the process and does not allow the manifest file to be embedded into the executable.

// Note:	TestStand installs the source code files for the default user interfaces in the <TestStand>\UserInterfaces and <TestStand Public>\UserInterfaces directories. 
//			To modify the installed user interfaces or to create new user interfaces, modify the files in the <TestStand Public>\UserInterfaces directory. 
//			You can use the read-only source files for the default user interfaces in the <TestStand>\UserInterfaces directory as a reference. 
//			National Instruments recommends that you track the changes you make to the user interface source code files so you can integrate the changes with any enhancements in future versions of the TestStand User Interfaces.

using System;
using System.Diagnostics;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Runtime.Versioning;
using System.Windows.Forms;
using NationalInstruments.TestStand.Grpc.Net.Server.OO;

// TestStand Core API 
using NationalInstruments.TestStand.Interop.API;

// TestStand User Interface Controls
using NationalInstruments.TestStand.Interop.UI;
using NationalInstruments.TestStand.Interop.UI.Support;

// .net specific functions for use with TestStand APIs (TSUtil)
using NationalInstruments.TestStand.Utility;

namespace TestExecServer
{
    /// <summary>
    /// Summary description for MainForm.
    /// </summary>
    public class MainForm : Form
    {
        private const int WM_QUERYENDSESSION = 0x11; // See Microsoft documentation.
        private const string WindowTitle = "Simple Test Executive Operator Interface Example - with gRPC server";

        private NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox axFilesComboBox;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox axSequencesComboBox;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axOpenFileButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axCloseFileButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxApplicationMgr axApplicationMgr;
        private System.Windows.Forms.Timer GCTimer;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axEntryPoint1Button;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axEntryPoint2Button;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axRunSelectedButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axCloseExecutionButton;
        private System.Windows.Forms.Label sequenceFileLabel;
        private System.Windows.Forms.Label sequenceLabel;
        private System.Windows.Forms.Label executionLabel;
        private System.Windows.Forms.Label waitForClientLabel;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxSequenceView axSequenceView;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxExecutionViewMgr axExecutionViewMgr;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxSequenceFileViewMgr axSequenceFileViewMgr;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox axExecutionsComboBox;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxReportView axReportView;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axBreakResumeButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axTerminateRestartButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axLoginLogoutButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axExitButton;
        private NationalInstruments.TestStand.Interop.UI.Ax.AxButton axTerminateAllButton;
        private System.ComponentModel.IContainer components;

        private bool _isHeadless;
        private NotifyIcon _notifyIcon;
        private string _serverAndPortInformation;

        // flag that will be set to true if the user tries to shut down windows
        private bool _sessionEnding = false;

        private readonly string[] _args;

        public MainForm(bool isHeadless, string[] args)
        {
            // Required for Windows Form Designer support
            InitializeComponent();

            _args = args;

            Text = WindowTitle;

            // NOTE: Add any constructor code after InitializeComponent call
            this.Icon = Properties.Resources.App;

            SetHeadlessState(isHeadless);
        }

        private void SetHeadlessState(bool isHeadless)
        {
            _isHeadless = isHeadless;
            if (_isHeadless)
            {
                var exitItem = new ToolStripMenuItem("Exit", null, (s, e) => Close());
                var contextMenuStrip = new ContextMenuStrip();
                contextMenuStrip.Items.Add(exitItem);

                _notifyIcon.ContextMenuStrip = contextMenuStrip;
                _notifyIcon.Visible = true;

                // Minimizing the window will hide the main window and remove it from the taskbar
                WindowState = FormWindowState.Minimized;

                // For a headless application, don't open the main window when double clicking on tray icon
                _notifyIcon.MouseDoubleClick -= NotifyIcon_MouseDoubleClick;
            }
        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }

                GrpcServer.Shutdown();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.axApplicationMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxApplicationMgr();
            this.axFilesComboBox = new NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox();
            this.axSequencesComboBox = new NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox();
            this.axOpenFileButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axCloseFileButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.GCTimer = new System.Windows.Forms.Timer(this.components);
            this.axExecutionViewMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxExecutionViewMgr();
            this.axSequenceFileViewMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxSequenceFileViewMgr();
            this.axEntryPoint1Button = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axEntryPoint2Button = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axRunSelectedButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axExecutionsComboBox = new NationalInstruments.TestStand.Interop.UI.Ax.AxComboBox();
            this.axCloseExecutionButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.sequenceFileLabel = new System.Windows.Forms.Label();
            this.sequenceLabel = new System.Windows.Forms.Label();
            this.executionLabel = new System.Windows.Forms.Label();
            this.waitForClientLabel = new System.Windows.Forms.Label();
            this.axSequenceView = new NationalInstruments.TestStand.Interop.UI.Ax.AxSequenceView();
            this.axReportView = new NationalInstruments.TestStand.Interop.UI.Ax.AxReportView();
            this.axBreakResumeButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axTerminateRestartButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axLoginLogoutButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axExitButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this.axTerminateAllButton = new NationalInstruments.TestStand.Interop.UI.Ax.AxButton();
            this._notifyIcon = new System.Windows.Forms.NotifyIcon(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.axApplicationMgr)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axFilesComboBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequencesComboBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axOpenFileButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axCloseFileButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExecutionViewMgr)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequenceFileViewMgr)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axEntryPoint1Button)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axEntryPoint2Button)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axRunSelectedButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExecutionsComboBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axCloseExecutionButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequenceView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axReportView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axBreakResumeButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTerminateRestartButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axLoginLogoutButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExitButton)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTerminateAllButton)).BeginInit();
            this.SuspendLayout();
            // 
            // axApplicationMgr
            // 
            this.axApplicationMgr.Location = new System.Drawing.Point(644, 332);
            this.axApplicationMgr.Name = "axApplicationMgr";
            this.axApplicationMgr.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axApplicationMgr.OcxState")));
            this.axApplicationMgr.Size = new System.Drawing.Size(32, 32);
            this.axApplicationMgr.TabIndex = 16;
            this.axApplicationMgr.ExitApplication += new System.EventHandler(this.ApplicationMgr_ExitApplication);
            this.axApplicationMgr.ReportError += new NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_ReportErrorEventHandler(this.ApplicationMgr_ReportError);
            this.axApplicationMgr.DisplaySequenceFile += new NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplaySequenceFileEventHandler(this.ApplicationMgr_DisplaySequenceFile);
            this.axApplicationMgr.DisplayExecution += new NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplayExecutionEventHandler(this.ApplicationMgr_DisplayExecution);
            // 
            // axFilesComboBox
            // 
            this.axFilesComboBox.Location = new System.Drawing.Point(112, 8);
            this.axFilesComboBox.Name = "axFilesComboBox";
            this.axFilesComboBox.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axFilesComboBox.OcxState")));
            this.axFilesComboBox.Size = new System.Drawing.Size(564, 22);
            this.axFilesComboBox.TabIndex = 1;
            // 
            // axSequencesComboBox
            // 
            this.axSequencesComboBox.Location = new System.Drawing.Point(112, 37);
            this.axSequencesComboBox.Name = "axSequencesComboBox";
            this.axSequencesComboBox.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axSequencesComboBox.OcxState")));
            this.axSequencesComboBox.Size = new System.Drawing.Size(564, 22);
            this.axSequencesComboBox.TabIndex = 4;
            // 
            // axOpenFileButton
            // 
            this.axOpenFileButton.Location = new System.Drawing.Point(709, 5);
            this.axOpenFileButton.Name = "axOpenFileButton";
            this.axOpenFileButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axOpenFileButton.OcxState")));
            this.axOpenFileButton.Size = new System.Drawing.Size(167, 26);
            this.axOpenFileButton.TabIndex = 2;
            // 
            // axCloseFileButton
            // 
            this.axCloseFileButton.Location = new System.Drawing.Point(709, 35);
            this.axCloseFileButton.Name = "axCloseFileButton";
            this.axCloseFileButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axCloseFileButton.OcxState")));
            this.axCloseFileButton.Size = new System.Drawing.Size(167, 26);
            this.axCloseFileButton.TabIndex = 5;
            // 
            // GCTimer
            // 
            this.GCTimer.Interval = 3000;
            this.GCTimer.Tick += new System.EventHandler(this.GCTimerTick);
            // 
            // axExecutionViewMgr
            // 
            this.axExecutionViewMgr.Location = new System.Drawing.Point(720, 331);
            this.axExecutionViewMgr.Name = "axExecutionViewMgr";
            this.axExecutionViewMgr.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axExecutionViewMgr.OcxState")));
            this.axExecutionViewMgr.Size = new System.Drawing.Size(32, 32);
            this.axExecutionViewMgr.TabIndex = 18;
            // 
            // axSequenceFileViewMgr
            // 
            this.axSequenceFileViewMgr.Location = new System.Drawing.Point(682, 331);
            this.axSequenceFileViewMgr.Name = "axSequenceFileViewMgr";
            this.axSequenceFileViewMgr.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axSequenceFileViewMgr.OcxState")));
            this.axSequenceFileViewMgr.Size = new System.Drawing.Size(32, 32);
            this.axSequenceFileViewMgr.TabIndex = 17;
            // 
            // axEntryPoint1Button
            // 
            this.axEntryPoint1Button.Location = new System.Drawing.Point(112, 63);
            this.axEntryPoint1Button.Name = "axEntryPoint1Button";
            this.axEntryPoint1Button.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axEntryPoint1Button.OcxState")));
            this.axEntryPoint1Button.Size = new System.Drawing.Size(187, 26);
            this.axEntryPoint1Button.TabIndex = 6;
            // 
            // axEntryPoint2Button
            // 
            this.axEntryPoint2Button.Location = new System.Drawing.Point(300, 63);
            this.axEntryPoint2Button.Name = "axEntryPoint2Button";
            this.axEntryPoint2Button.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axEntryPoint2Button.OcxState")));
            this.axEntryPoint2Button.Size = new System.Drawing.Size(187, 26);
            this.axEntryPoint2Button.TabIndex = 7;
            // 
            // axRunSelectedButton
            // 
            this.axRunSelectedButton.Location = new System.Drawing.Point(488, 63);
            this.axRunSelectedButton.Name = "axRunSelectedButton";
            this.axRunSelectedButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axRunSelectedButton.OcxState")));
            this.axRunSelectedButton.Size = new System.Drawing.Size(187, 26);
            this.axRunSelectedButton.TabIndex = 8;
            // 
            // axExecutionsComboBox
            // 
            this.axExecutionsComboBox.Location = new System.Drawing.Point(112, 95);
            this.axExecutionsComboBox.Name = "axExecutionsComboBox";
            this.axExecutionsComboBox.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axExecutionsComboBox.OcxState")));
            this.axExecutionsComboBox.Size = new System.Drawing.Size(564, 22);
            this.axExecutionsComboBox.TabIndex = 10;
            // 
            // axCloseExecutionButton
            // 
            this.axCloseExecutionButton.Location = new System.Drawing.Point(709, 92);
            this.axCloseExecutionButton.Name = "axCloseExecutionButton";
            this.axCloseExecutionButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axCloseExecutionButton.OcxState")));
            this.axCloseExecutionButton.Size = new System.Drawing.Size(167, 26);
            this.axCloseExecutionButton.TabIndex = 11;
            // 
            // sequenceFileLabel
            // 
            this.sequenceFileLabel.Location = new System.Drawing.Point(5, 12);
            this.sequenceFileLabel.Name = "sequenceFileLabel";
            this.sequenceFileLabel.Size = new System.Drawing.Size(96, 16);
            this.sequenceFileLabel.TabIndex = 0;
            this.sequenceFileLabel.Text = "Sequence Files:";
            // 
            // sequenceLabel
            // 
            this.sequenceLabel.Location = new System.Drawing.Point(5, 40);
            this.sequenceLabel.Name = "sequenceLabel";
            this.sequenceLabel.Size = new System.Drawing.Size(96, 16);
            this.sequenceLabel.TabIndex = 3;
            this.sequenceLabel.Text = "Sequences:";
            // 
            // executionLabel
            // 
            this.executionLabel.Location = new System.Drawing.Point(5, 100);
            this.executionLabel.Name = "executionLabel";
            this.executionLabel.Size = new System.Drawing.Size(96, 16);
            this.executionLabel.TabIndex = 9;
            this.executionLabel.Text = "Executions:";
            // 
            // waitForClientLabel
            //
            this.waitForClientLabel.AutoSize = true;
            this.waitForClientLabel.Location = new System.Drawing.Point(5, 575);
            this.waitForClientLabel.Name = "waitForClientLabel";
            this.waitForClientLabel.Size = new System.Drawing.Size(96, 16);
            this.waitForClientLabel.TabIndex = 20;
            this.waitForClientLabel.Text = "";
            // 
            // axSequenceView
            // 
            this.axSequenceView.Location = new System.Drawing.Point(5, 125);
            this.axSequenceView.Name = "axSequenceView";
            this.axSequenceView.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axSequenceView.OcxState")));
            this.axSequenceView.Size = new System.Drawing.Size(871, 200);
            this.axSequenceView.TabIndex = 12;
            // 
            // axReportView
            // 
            this.axReportView.Location = new System.Drawing.Point(5, 361);
            this.axReportView.Name = "axReportView";
            this.axReportView.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axReportView.OcxState")));
            this.axReportView.Size = new System.Drawing.Size(871, 205);
            this.axReportView.TabIndex = 19;
            // 
            // axBreakResumeButton
            // 
            this.axBreakResumeButton.Location = new System.Drawing.Point(5, 330);
            this.axBreakResumeButton.Name = "axBreakResumeButton";
            this.axBreakResumeButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axBreakResumeButton.OcxState")));
            this.axBreakResumeButton.Size = new System.Drawing.Size(167, 26);
            this.axBreakResumeButton.TabIndex = 13;
            // 
            // axTerminateRestartButton
            // 
            this.axTerminateRestartButton.Location = new System.Drawing.Point(176, 330);
            this.axTerminateRestartButton.Name = "axTerminateRestartButton";
            this.axTerminateRestartButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axTerminateRestartButton.OcxState")));
            this.axTerminateRestartButton.Size = new System.Drawing.Size(167, 26);
            this.axTerminateRestartButton.TabIndex = 14;
            // 
            // axLoginLogoutButton
            // 
            this.axLoginLogoutButton.Location = new System.Drawing.Point(539, 571);
            this.axLoginLogoutButton.Name = "axLoginLogoutButton";
            this.axLoginLogoutButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axLoginLogoutButton.OcxState")));
            this.axLoginLogoutButton.Size = new System.Drawing.Size(167, 26);
            this.axLoginLogoutButton.TabIndex = 21;
            // 
            // axExitButton
            // 
            this.axExitButton.Location = new System.Drawing.Point(710, 571);
            this.axExitButton.Name = "axExitButton";
            this.axExitButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axExitButton.OcxState")));
            this.axExitButton.Size = new System.Drawing.Size(167, 26);
            this.axExitButton.TabIndex = 22;
            // 
            // axTerminateAllButton
            // 
            this.axTerminateAllButton.Location = new System.Drawing.Point(347, 330);
            this.axTerminateAllButton.Name = "axTerminateAllButton";
            this.axTerminateAllButton.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axTerminateAllButton.OcxState")));
            this.axTerminateAllButton.Size = new System.Drawing.Size(167, 26);
            this.axTerminateAllButton.TabIndex = 15;
            // 
            // notifyIcon
            // 
            this._notifyIcon.Icon = this.Icon;
            this._notifyIcon.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.NotifyIcon_MouseDoubleClick);
            // 
            // MainForm
            // 
            this.ClientSize = new System.Drawing.Size(882, 604);
            this.Controls.Add(this.axTerminateAllButton);
            this.Controls.Add(this.axExitButton);
            this.Controls.Add(this.axSequenceView);
            this.Controls.Add(this.axLoginLogoutButton);
            this.Controls.Add(this.axTerminateRestartButton);
            this.Controls.Add(this.axBreakResumeButton);
            this.Controls.Add(this.axReportView);
            this.Controls.Add(this.executionLabel);
            this.Controls.Add(this.sequenceLabel);
            this.Controls.Add(this.sequenceFileLabel);
            this.Controls.Add(this.waitForClientLabel);
            this.Controls.Add(this.axExecutionsComboBox);
            this.Controls.Add(this.axRunSelectedButton);
            this.Controls.Add(this.axEntryPoint2Button);
            this.Controls.Add(this.axEntryPoint1Button);
            this.Controls.Add(this.axSequenceFileViewMgr);
            this.Controls.Add(this.axExecutionViewMgr);
            this.Controls.Add(this.axCloseFileButton);
            this.Controls.Add(this.axOpenFileButton);
            this.Controls.Add(this.axCloseExecutionButton);
            this.Controls.Add(this.axSequencesComboBox);
            this.Controls.Add(this.axFilesComboBox);
            this.Controls.Add(this.axApplicationMgr);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Closing += new System.ComponentModel.CancelEventHandler(this.MainForm_Closing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.Resize += new System.EventHandler(this.MainForm_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.axApplicationMgr)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axFilesComboBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequencesComboBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axOpenFileButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axCloseFileButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExecutionViewMgr)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequenceFileViewMgr)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axEntryPoint1Button)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axEntryPoint2Button)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axRunSelectedButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExecutionsComboBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axCloseExecutionButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axSequenceView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axReportView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axBreakResumeButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTerminateRestartButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axLoginLogoutButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axExitButton)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTerminateAllButton)).EndInit();
            this.ResumeLayout(false);

        }
        #endregion

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Application.SetHighDpiMode(HighDpiMode.DpiUnaware);

            bool isHeadless = Array.Exists(args, arg => string.Equals(arg, "/headless", StringComparison.OrdinalIgnoreCase));
            var form = new MainForm(isHeadless, args);

            // Specify an action to perform if waiting on a client event reply in the GUI thread. This is optional. It will improve UI responsiveness
            // of the server app when clients go unresponsive and a message at the bottom left of the main form will inform a user who is interacting
            // with the server app when the progress of the app is necessarily impeeded due to waiting for client event responses or for the corresponding
            // timeouts to expire.
            ConnectionFactory.WaitLoopDelegate = (WaitLoopStates waitLoopState, double elapsedWaitTime) =>
            {
                if (!form.InvokeRequired)  // if we are waiting for a grpc event reply in the gui thread...
                {
                    if (waitLoopState == WaitLoopStates.Ended)
                    {
                        form.waitForClientLabel.Text = string.Empty; // clear wait message
                                                                     // form.Enabled = true;  // see comment on form.Enabled = false
                    }
                    else
                    {
                        // To avoid event-loop reentrancy, disable the UI before calling DoEvents, just like a Modal dialog disables a
                        // parent window  before running its nested event loop
                        // form.Enabled = false; // actually not doing this because disabling the form prevents dragging and makes the UI look hung even if it isn't. A more targeted disabling would be better.

                        form.waitForClientLabel.Text = $"Waiting For Client {elapsedWaitTime:F1}";

                        Application.DoEvents(); // process events so the gui thread isn't hung while waiting
                    }
                }
            };

            GrpcServer.StartupException += (_, exception) =>
            {
                form.Invoke(() =>
                {
                    form.Activate();

                    // Show the error message in the UI thread.
                    var message = $"{exception.Message}" +
                                    Environment.NewLine +
                                    Environment.NewLine +
                                    $"You can change the port number in the service_config.json file.";

                    form.axApplicationMgr.RaiseError(errorCode: exception.HResult, message);
                    Application.Exit();
                });
            };

            ApplicationWrapper.Run(form);
        }

        private void MainForm_Load(object sender, System.EventArgs e)
        {
            try
            {
                // If this UI is running in a CLR other than the one TestStand uses,
                // then it needs its own GCTimer for that version of the CLR. If it's running in the
                // same CLR as TestStand then the engine's gctimer enabled by the ApplicationMgr
                // is sufficient. See the API help for Engine.DotNetGarbageCollectionInterval for more details.
                if (Environment.Version.ToString() != axApplicationMgr.GetEngine().DotNetCLRVersion)
                    this.GCTimer.Enabled = true;

                // connect TestStand comboboxes 
                axSequenceFileViewMgr.ConnectSequenceFileList(axFilesComboBox.GetOcx(), true);
                axSequenceFileViewMgr.ConnectSequenceList(axSequencesComboBox.GetOcx());

                // specify what information to display in each execution list combobox entry (the expression string looks extra complicated here because we have to escape the quotes for the C# compiler.)
                axExecutionViewMgr.ConnectExecutionList(axExecutionsComboBox.GetOcx()).DisplayExpression = @"""%CurrentExecution% - "" + (""%UUTSerialNumber%"" == """" ? """" : (ResStr(""TSUI_OI_MAIN_PANEL"",""SERIAL_NUMBER"") + "" %UUTSerialNumber% - "")) + (""%TestSocketIndex%"" == """" ? """" : (ResStr(""TSUI_OI_MAIN_PANEL"",""SOCKET_NUMBER"") + "" %TestSocketIndex% - "")) + ""%ModelState%""";

                // connect sequence view to execution view manager									  
                axExecutionViewMgr.ConnectExecutionView(axSequenceView.GetOcx(), ExecutionViewOptions.ExecutionViewConnection_NoOptions);

                // connect report view to execution view manager									  
                axExecutionViewMgr.ConnectReportView(axReportView.GetOcx());

                // connect TestStand buttons to commands
                axExecutionViewMgr.ConnectCommand(axCloseExecutionButton.GetOcx(), CommandKinds.CommandKind_Close, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axApplicationMgr.ConnectCommand(axTerminateAllButton.GetOcx(), CommandKinds.CommandKind_TerminateAll, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axApplicationMgr.ConnectCommand(axLoginLogoutButton.GetOcx(), CommandKinds.CommandKind_LoginLogout, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axApplicationMgr.ConnectCommand(axExitButton.GetOcx(), CommandKinds.CommandKind_Exit, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axSequenceFileViewMgr.ConnectCommand(axOpenFileButton.GetOcx(), CommandKinds.CommandKind_OpenSequenceFiles, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axSequenceFileViewMgr.ConnectCommand(axCloseFileButton.GetOcx(), CommandKinds.CommandKind_Close, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axSequenceFileViewMgr.ConnectCommand(axEntryPoint1Button.GetOcx(), CommandKinds.CommandKind_ExecutionEntryPoints_Set, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axSequenceFileViewMgr.ConnectCommand(axEntryPoint2Button.GetOcx(), CommandKinds.CommandKind_ExecutionEntryPoints_Set, 1, CommandConnectionOptions.CommandConnection_EnableImage);
                axSequenceFileViewMgr.ConnectCommand(axRunSelectedButton.GetOcx(), CommandKinds.CommandKind_RunCurrentSequence, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axExecutionViewMgr.ConnectCommand(axBreakResumeButton.GetOcx(), CommandKinds.CommandKind_BreakResume, 0, CommandConnectionOptions.CommandConnection_EnableImage);
                axExecutionViewMgr.ConnectCommand(axTerminateRestartButton.GetOcx(), CommandKinds.CommandKind_TerminateRestart, 0, CommandConnectionOptions.CommandConnection_EnableImage);

                // show all step groups at once in the sequence view
                axExecutionViewMgr.StepGroupMode = StepGroupModes.StepGroupMode_AllGroups;

                // this is a server, no sense in prompting to log in a local user
                axApplicationMgr.GetEngine().StationOptions.LoginOnStart = false;
                axApplicationMgr.GetEngine().StationOptions.EnableUserPrivilegeChecking = false;

                // make the managers available as named grpc globals
                ConnectionFactory.ServerGlobalScope.ToInstanceId(axApplicationMgr.GetOcx(), true, "ApplicationMgr");
                ConnectionFactory.ServerGlobalScope.ToInstanceId(axSequenceFileViewMgr.GetOcx(), true, "SequenceFileViewMgr");
                ConnectionFactory.ServerGlobalScope.ToInstanceId(axExecutionViewMgr.GetOcx(), true, "ExecutionViewMgr");

                axApplicationMgr.Start();   // start up the TestStand User Interface Components.

                // create all grpc-api objects in the UI thread in to make sure that any UI objects (Label, SequenceView...) are created in the UI thread
                ConnectionFactory.ObjectCreationDelegate = (Action objectCreator, Type objectType) => this.Invoke(objectCreator);

                // Start the gRPC server after the TestStand application is fully initialized..
                GrpcServer.Start(_args);
            }
            catch (Exception theException)
            {
                MessageBox.Show(this, theException.Message, "Error");
                Application.Exit();
            }

            if (string.IsNullOrEmpty(GrpcServer.ErrorMessage))
            {
                _serverAndPortInformation = Dns.GetHostEntry(Dns.GetHostName()).HostName + ":" + GrpcServer.Port;

                string ipaddressAndPort = " [" + _serverAndPortInformation + "]";
                string typeOfConnection = GrpcServer.UsesHttps ? " [Secure]" : " [Not secure]";
                Text += typeOfConnection + ipaddressAndPort;

                string trayText = "TestStand gRPC Server" + typeOfConnection + ipaddressAndPort;
                _notifyIcon.BalloonTipTitle = trayText;
                _notifyIcon.Text = trayText;

                AddCopyServerInformationMenuItemToSystemMenu();

                // Enable finding example sequence files in the location of the executable.
                AddExampleFilesDirectoryToSearchDirectories();
            }
            else if (_isHeadless)
            {
                string message = "Failed to initialize gRPC service with following error(s):\n\n" + GrpcServer.ErrorMessage;

                if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
                {
                    WriteErrorToEventLog(message);
                }

                // For a headless application, there is no point of continuning if there is no gRPC service. So, close the application.
                Close();
            }
            else
            {
                Text += " [No gRPC Service]";

                // Try to show the error dialog after the MainForm becomes visible. It is not always guarantee that 
                // MainForm will show before the error dialog when using BeginInvoke, however, in most cases it does.
                BeginInvoke(() =>
                {
                    string message = "Failed to initialize gRPC service with following error(s):\n\n" + GrpcServer.ErrorMessage;
                    axApplicationMgr.RaiseError((int)TSError.TS_Err_OperationFailed, message);
                });
            }
        }

        private void AddExampleFilesDirectoryToSearchDirectories()
        {
            string examplesDirectory = LongPath.Combine(LongPath.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "ExampleFiles");

            SearchDirectories searchDirectories = axApplicationMgr.GetEngine().SearchDirectories;
            foreach (SearchDirectory searchDirectory in searchDirectories)
            {
                if (!string.IsNullOrEmpty(searchDirectory.Path) &&
                    String.Compare(searchDirectory.Path, examplesDirectory, StringComparison.OrdinalIgnoreCase) == 0)
                {
                    searchDirectory.Disabled = false;
                    return;
                }
            }

            searchDirectories.Insert(examplesDirectory);
        }

        // handle request to close form (via Windows close box, for example)
        private void MainForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            // Don't set e.Cancel to true if windows is shutting down.
            // Doing so would prevent windows from shutting down or logging out.
            if (!_sessionEnding)
            {
                // initiate shutdown and cancel close if shutdown is not complete.  The applicationMgr will
                // send the ExitApplication event when shutdown is complete and we can close then
                if (axApplicationMgr.Shutdown() == false)
                    e.Cancel = true;
            }

            if (!e.Cancel)
            {
                // Since server is shutting down, discard all connections to make sure
                // all objects in those connections are also released.
                ConnectionFactory.DiscardAllConnections();
            }
        }

        protected override void WndProc(ref Message msg)
        {
            const int WM_SYSCOMMAND = 0x0112;

            // set the sessionEnding flag so I will know the form is closing because the user
            // is trying to shutdown, restart, or logoff windows
            if (msg.Msg == WM_QUERYENDSESSION)
            {
                _sessionEnding = true;
                Application.Exit();
            }
            else if (msg.Msg == WM_SYSCOMMAND)
            {
                if (msg.WParam.ToInt32() == ID_COPY_SERVER_INFO)
                {
                    Clipboard.SetText(_serverAndPortInformation);
                }
            }

            base.WndProc(ref msg);
        }

        // It is now ok to exit, close the form
        private void ApplicationMgr_ExitApplication(object sender, System.EventArgs e)
        {
            Environment.ExitCode = this.axApplicationMgr.ExitCode;
            Close();

            TSHelper.DoSynchronousGCForCOMObjectDestruction();
        }

        // ApplicationMgr sends this event to handle any errors it detects.  For example, if a TestStand menu command
        // generates an error, this handler displays it
        private void ApplicationMgr_ReportError(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_ReportErrorEvent e)
        {
            MessageBox.Show(this, ErrorMessage.AppendCodeAndDescription(this.axApplicationMgr, e.errorMessage, e.errorCode), "Error", MessageBoxButtons.OK, MessageBoxIcon.Stop);
        }

        // the ApplicationMgr sends this event to request that the UI display a particular execution
        private void ApplicationMgr_DisplayExecution(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplayExecutionEvent e)
        {
            // bring application to front if we hit a breakpoint
            if (e.reason == ExecutionDisplayReasons.ExecutionDisplayReason_Breakpoint || e.reason == ExecutionDisplayReasons.ExecutionDisplayReason_BreakOnRunTimeError)
                this.Activate();

            axExecutionViewMgr.Execution = e.exec;
        }

        // the ApplicationMgr sends this event to request that the UI display a particular sequence file
        private void ApplicationMgr_DisplaySequenceFile(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplaySequenceFileEvent e)
        {
            axSequenceFileViewMgr.SequenceFile = e.file;
        }

        // Release all objects periodically.  .NET lets COM objects pile up on the managed heap, seemingly even objects you don't know about such
        // as parameters to unhandled ActiveX events.  This timer ensures that all COM objects are released in a timely manner,
        // thus preventing the performance hiccup that could occur when .NET finally decides to collect garbage. Also, this timer
        // ensures that actions triggered by object destruction run in a timely manner. For example: sequence file unload callbacks.
        private void GCTimerTick(object sender, System.EventArgs e)
        {
            GC.Collect(GC.MaxGeneration, GCCollectionMode.Forced, false); // force .net garbage collection
        }

        // Check whether the form has been minimized and if so, hide it from the Taskbar
        // and set the NotifyIcon's visibility to True to display it in the system tray.
        private void MainForm_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                Hide();
                _notifyIcon.Visible = true;
            }
        }

        // Handle NotifyIcon's MouseDoubleClick event and in its response we will
        // show the app on the Taskbar, un-minimize it, and hide the system tray icon.
        private void NotifyIcon_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            Show();
            this.WindowState = FormWindowState.Normal;
            _notifyIcon.Visible = false;
        }

        [SupportedOSPlatform("windows")]  // Added this to remove warning CA1416
        private void WriteErrorToEventLog(string textToLog)
        {
            const string logSource = "TestStand gRPC Server";

            if (!EventLog.SourceExists(logSource))
            {
                EventLog.CreateEventSource(logSource, "Application");
            }

            EventLog.WriteEntry(logSource, textToLog, EventLogEntryType.Error);
        }

        private const int MF_BYPOSITION = 0x0400;
        private const int MF_STRING = 0x0000;
        private const int MENU_POSITION = 5;
        private const int ID_COPY_SERVER_INFO = 1;

        private void AddCopyServerInformationMenuItemToSystemMenu()
        {
            IntPtr systemMenuPtr = GetSystemMenu(Handle, false);
            HandleRef systemMenuHandle = new HandleRef(null, systemMenuPtr);
            InsertMenu(systemMenuHandle, MENU_POSITION, MF_BYPOSITION | MF_STRING, ID_COPY_SERVER_INFO, "Copy Server Information to Clipboard");
        }

        [DllImport("user32.dll")]
        private static extern IntPtr GetSystemMenu(IntPtr hWnd, bool bRevert);

        [DllImport("user32.dll", CharSet = CharSet.Unicode, ExactSpelling = false)]
        public extern static bool InsertMenu(HandleRef hMenu, UInt32 uPosition, UInt32 uFlags, UInt32 uIDNewItem, string lpNewItem);
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/MainForm.resx sha256=f94da6609cb84c8eba92d847baccb0f657487df8b159a3563d6d793f14fc69aa bytes=17272 -->
## FILE: Server/UI/MainForm.resx

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/MainForm.resx`
- sha256: `f94da6609cb84c8eba92d847baccb0f657487df8b159a3563d6d793f14fc69aa`
- bytes: 17272

````text
<root>
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="axApplicationMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAA/gAAAAIB
        AAAAAQAAAAAAAAAAAAAAAOkAAAAXAQEAAU8DAABPAwAAAQEBAgAAACYAAABDAEUAbgBnAGkAbgBlAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAADAAAAGAAAAEMAQwBvAG4AZgBpAGcARgBpAGwAZQAAAAEA
        AAAAAgAAAAEAAgAAAFQAAAAlAFQAZQBzAHQAUwB0AGEAbgBkAEwAbwBjAGEAbABBAHAAcABEAGEAdABh
        ACUAXABVAHMAZQByAEkAbgB0AGUAcgBmAGEAYwBlAC4AeABtAGwAAAACAAG4CwAAAAMAAAABAC0AAAAH
        AAAAARAAAAEQAAABAQs=
</value>
  </data>
  <data name="axFilesComboBox.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAegAAAAIB
        AAAAAQAAAAAAAAAAAAAAAGUAAAAZAQEAAPkBAAAWAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmEgAAgP///wAAAAAAAQAAAAIAAAABAGQAAAAQAAAA
        AQs=
</value>
  </data>
  <data name="axSequencesComboBox.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAegAAAAIB
        AAAAAQAAAAAAAAAAAAAAAGUAAAAZAQEAAPkBAAAWAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmEgAAgP///wAAAAAAAQAAAAIAAAABAGQAAAAQAAAA
        AQs=
</value>
  </data>
  <data name="axOpenFileButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAApwAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJIAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABQAAABP
        AFAARQBOAF8ARgBJAEwARQAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axCloseFileButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAqQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJQAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABYAAABD
        AEwATwBTAEUAXwBGAEkATABFAAAA////AAAAAAABAAAAAwAAAAEBAwAAAAAAAAABCw==
</value>
  </data>
  <data name="axExecutionViewMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAXAAAAAIB
        AAAAAQAAAAAAAAAAAAAAAEcAAAAZAQEAAU8DAABPAwAAAQIAAAAoAAAAQwBFAHgAZQBEAGkAcwBwAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAABAQAAAAs=
</value>
  </data>
  <data name="axSequenceFileViewMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAXAAAAAIB
        AAAAAQAAAAAAAAAAAAAAAEcAAAAZAQEAAU8DAABPAwAAAQIAAAAoAAAAQwBTAGUAcQBEAGkAcwBwAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAABAQAAAAs=
</value>
  </data>
  <data name="axEntryPoint1Button.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABoAAABF
        AE4AVABSAFkAXwBQAE8ASQBOAFQAMQAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axEntryPoint2Button.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABoAAABF
        AE4AVABSAFkAXwBQAE8ASQBOAFQAMgAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axRunSelectedButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAvwAAAAIB
        AAAAAQAAAAAAAAAAAAAAAKoAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAACwAAABS
        AFUATgBfAFMARQBMAEUAQwBUAEUARABfAFMARQBRAFUARQBOAEMARQAAAP///wAAAAAAAQAAAAMAAAAB
        AQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axExecutionsComboBox.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAegAAAAIB
        AAAAAQAAAAAAAAAAAAAAAGUAAAAZAQEAAPkBAAAWAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmEgAAgP///wAAAAAAAQAAAAIAAAABAGQAAAAQAAAA
        AQs=
</value>
  </data>
  <data name="axCloseExecutionButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAswAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJ4AAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAACAAAABD
        AEwATwBTAEUAXwBFAFgARQBDAFUAVABJAE8ATgAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axSequenceView.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAjAUAAAIB
        AAAAAQAAAAAAAAAAAAAAAHcFAAAXAQEAABADAADIAAAAAf//AAD//wAAAAAIAACAgICAAAUAAIDAwMAA
        AgAAAAADUuMLkY/OEZ3jAKoAS7hRAQAAAJABREIBABRNaWNyb3NvZnQgU2FucyBTZXJpZgMAAAAAA1Lj
        C5GPzhGd4wCqAEu4UQEAAACQAURCAQAUTWljcm9zb2Z0IFNhbnMgU2VyaWYEAAAAAANS4wuRj84RneMA
        qgBLuFEBAAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmBQAAAAQAAAAKAAAATgBhAG0AZQAAAAIA
        AAAAAL4AAAABAQAAAAIAAAAAAAIAAAAAAAoAAABOAGEAbQBlAAAAAAAAABgAAABEAGUAcwBjAHIAaQBw
        AHQAaQBvAG4AAAACAAAAAAAiAQAAAQMAAAACAAAAAAACAAAAAAAYAAAARABlAHMAYwByAGkAcAB0AGkA
        bwBuAAAAAAAAAB4AAABFAHgAZQBjAHUAdABpAG8AbgAgAEYAbABvAHcAAAACAAAAAACWAAAAAQQAAAAC
        AAAAAAACAAAAAAAeAAAARQB4AGUAYwB1AHQAaQBvAG4AIABGAGwAbwB3AAAAAAAAAA4AAABTAHQAYQB0
        AHUAcwAAAAIAAAAAAHkAAAABBQAAAAIAAAAAADIDAABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4A
        UgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0APQAgACIAIgAgAD8AIAAtADEAIAA6ACAAKABSAHUA
        bgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0APQAgACIA
        RgBhAGkAbABlAGQAIgAgAHwAfAAgAFIAdQBuAFMAdABhAHQAZQAuAFMAdABlAHAALgBSAGUAcwB1AGwA
        dAAuAFMAdABhAHQAdQBzACAAPQA9ACAAIgBFAHIAcgBvAHIAIgApACAAPwAgAHQAcwBSAGUAZAAgADoA
        IABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0A
        PQAgACIAUABhAHMAcwBlAGQAIgAgAD8AIAB0AHMARwByAGUAZQBuACAAOgAgAFIAdQBuAFMAdABhAHQA
        ZQAuAFMAdABlAHAALgBSAGUAcwB1AGwAdAAuAFMAdABhAHQAdQBzACAAPQA9ACAAIgBTAGsAaQBwAHAA
        ZQBkACIAIAA/ACAAdABzAEwAaQBnAGgAdABHAHIAYQB5ACAAOgAgACgAUgB1AG4AUwB0AGEAdABlAC4A
        UwB0AGUAcAAuAFIAZQBzAHUAbAB0AC4AUwB0AGEAdAB1AHMAIAA9AD0AIAAiAFIAdQBuAG4AaQBuAGcA
        IgAgAAoAIAB8AHwAIABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQA
        YQB0AHUAcwAgAD0APQAgACIATABvAG8AcABpAG4AZwAiACkAIAA/ACAAdABzAE0AYQBnAGUAbgB0AGEA
        IAA6ACAAUgB1AG4AUwB0AGEAdABlAC4AUwB0AGUAcAAuAFIAZQBzAHUAbAB0AC4AUwB0AGEAdAB1AHMA
        IAA9AD0AIAAiAFQAZQByAG0AaQBuAGEAdABlAGQAIgAgAD8AIAB0AHMAQgBsAHUAZQAgADoAIAB0AHMA
        QwB5AGEAbgAAAA4AAABTAHQAYQB0AHUAcwAAAAEAAAABAAIAAAAAAAIAAAAAAAMAAAAAAAAAEAAAAAEA
        AAABAAAAAQAAAP////8DAAAAAwAAAAEBBAAAAAAAAAAB//8/AAAACw==
</value>
  </data>
  <data name="axReportView.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAhQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAHAAAAAXAQEAABADAADNAAAAAQAAAAAJAAAAAQEBAQEBAQEBAQABAAAABQAA
        gAgAAIABAwAAAAMAAAABAQQAAAAAAAAAAQIAAAAAA1LjC5GPzhGd4wCqAEu4UQEAAACQAZBfAQALQ291
        cmllciBOZXcLAAAACw==
</value>
  </data>
  <data name="axBreakResumeButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABoAAABC
        AFIARQBBAEsALwBSAEUAUwBVAE0ARQAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axTerminateRestartButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABoAAABU
        AEUAUgBNAC8AUgBFAFMAVABBAFIAVAAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axLoginLogoutButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABoAAABM
        AE8ARwBJAE4ALwBMAE8ARwBPAFUAVAAAAP///wAAAAAAAQAAAAMAAAABAQMAAAAAAAAAAQs=
</value>
  </data>
  <data name="axExitButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAnQAAAAIB
        AAAAAQAAAAAAAAAAAAAAAIgAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAAAoAAABF
        AFgASQBUAAAA////AAAAAAABAAAAAwAAAAEBAwAAAAAAAAABCw==
</value>
  </data>
  <data name="axTerminateAllButton.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj01LjAuMy4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAArwAAAAIB
        AAAAAQAAAAAAAAAAAAAAAJoAAAAZAQEAAKcAAAAaAAAAAQH///8CAAAAAANS4wuRj84RneMAqgBLuFEB
        AAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmAAAAAA8AAIAAAAAAAQAAAAIAAAAAAAAAABwAAABU
        AEUAUgBNAEkATgBBAFQARQBfAEEATABMAAAA////AAAAAAABAAAAAwAAAAEBAwAAAAAAAAABCw==
</value>
  </data>
  <metadata name="$this.TrayHeight" type="System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e">
    <value>25</value>
  </metadata>
</root>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/Properties/Resources.Designer.cs sha256=7d213cc19d14b75fd191a7c79b6d21cdf9513689c9a4c9ff71fd032c169dbc4e bytes=3236 -->
## FILE: Server/UI/Properties/Resources.Designer.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/Properties/Resources.Designer.cs`
- sha256: `7d213cc19d14b75fd191a7c79b6d21cdf9513689c9a4c9ff71fd032c169dbc4e`
- bytes: 3236

````csharp
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace TestExecServer.Properties {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "4.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Resources {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Resources() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("TestExecServer.Properties.Resources", typeof(Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.Drawing.Icon similar to (Icon).
        /// </summary>
        internal static System.Drawing.Icon App {
            get {
                object obj = ResourceManager.GetObject("App", resourceCulture);
                return ((System.Drawing.Icon)(obj));
            }
        }
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/Properties/Resources.resx sha256=f80165af12cb3668d95f9cdd711418b0b2e68d1fa97f611b12d4268eb0b59ed5 bytes=6181 -->
## FILE: Server/UI/Properties/Resources.resx

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/Properties/Resources.resx`
- sha256: `f80165af12cb3668d95f9cdd711418b0b2e68d1fa97f611b12d4268eb0b59ed5`
- bytes: 6181

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <assembly alias="System.Windows.Forms" name="System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
  <data name="App" type="System.Resources.ResXFileRef, System.Windows.Forms">
    <value>..\App.ico;System.Drawing.Icon, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a</value>
  </data>
</root>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/Readme.md sha256=36d57a94bd02adec6c354c46552a27edf31911241a836879bfc9512f4b4813d2 bytes=1605 -->
## FILE: Server/UI/Readme.md

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/Readme.md`
- sha256: `36d57a94bd02adec6c354c46552a27edf31911241a836879bfc9512f4b4813d2`
- bytes: 1605

````markdown
# About This Example
This example is a copy of `<TestStand>\UserInterfaces\Simple\CSharp` that has been extended to provide a gRPC server for the TestStand API.

This example can run as a headless server. To enable the headless option, pass the command line argument `/headless` when running the server.
If an error occurs while starting the gRPC service, the server will automatically shutdown and the error will be logged in the Windows Event Log.
When running as a headless server, a tray icon will appear on the taskbar that allows you to close the server. To close the server, right-click
on the tray icon and select Exit.

# To Do Items:

- Modify `axApplicationMgr_ReportError` to do whatever is appropriate when the server detects an error. Displaying a message box is probably not a good idea for a server.

- Modify `StartupTestStandGrpc.cs` to setup your grpc settings, including port selection, certificate settings, and any additional services you want to publish.

- Arrange to hide the main window if that is needed for the application. Otherwise leave it visible to aid with debugging. Here is how you can [hide a WinForms](https://stackoverflow.com/questions/683896/any-way-to-create-a-hidden-main-window-in-c/4913580) window.

- If the project is not finding its nuget dependency of `NationalInstruments.TestStand.gRPC.Server (0.5.0-*)`, add `https://api.nuget.org/v3/index.json` as a package source. Here is the link to [download the NationalInstruments.TestStand.gRPC.Server](https://www.nuget.org/packages?q=NationalInstruments.TestStand.gRPC.Server) nuget package.
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/TestExecServer.csproj sha256=8d4535340eac9ecaaa1642615d55e37a70412541b0964193bec7d3fdaa8694d9 bytes=7505 -->
## FILE: Server/UI/TestExecServer.csproj

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/TestExecServer.csproj`
- sha256: `8d4535340eac9ecaaa1642615d55e37a70412541b0964193bec7d3fdaa8694d9`
- bytes: 7505

````xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net6.0-windows</TargetFramework>
    <ProjectType>Local</ProjectType>
    <ApplicationIcon>App.ico</ApplicationIcon>
    <AssemblyKeyContainerName>
    </AssemblyKeyContainerName>
    <AssemblyOriginatorKeyFile>
    </AssemblyOriginatorKeyFile>
    <DefaultClientScript>JScript</DefaultClientScript>
    <DefaultHTMLPageLayout>Grid</DefaultHTMLPageLayout>
    <DefaultTargetSchema>IE50</DefaultTargetSchema>
    <DelaySign>false</DelaySign>
    <OutputType>WinExe</OutputType>
    <RunPostBuildEvent>OnBuildSuccess</RunPostBuildEvent>
    <StartupObject>
    </StartupObject>
    <ApplicationManifest>TestExecServer.exe.manifest</ApplicationManifest>
    <IsWebBootstrapper>false</IsWebBootstrapper>
    <PublishUrl>publish\</PublishUrl>
    <Install>true</Install>
    <InstallFrom>Disk</InstallFrom>
    <UpdateEnabled>false</UpdateEnabled>
    <UpdateMode>Foreground</UpdateMode>
    <UpdateInterval>7</UpdateInterval>
    <UpdateIntervalUnits>Days</UpdateIntervalUnits>
    <UpdatePeriodically>false</UpdatePeriodically>
    <UpdateRequired>false</UpdateRequired>
    <MapFileExtensions>true</MapFileExtensions>
    <ApplicationRevision>0</ApplicationRevision>
    <ApplicationVersion>1.0.0.%2a</ApplicationVersion>
    <UseApplicationTrust>false</UseApplicationTrust>
    <BootstrapperEnabled>true</BootstrapperEnabled>
    <GenerateAssemblyInfo>false</GenerateAssemblyInfo>
    <UseWindowsForms>true</UseWindowsForms>
    <ImportWindowsDesktopTargets>true</ImportWindowsDesktopTargets>
	<Platforms>x86;x64</Platforms>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|x86' ">
    <OutputPath>bin\x86\Debug\</OutputPath>
    <BaseAddress>285212672</BaseAddress>
    <UseVSHostingProcess>false</UseVSHostingProcess>
    <CodeAnalysisRuleSet>AllRules.ruleset</CodeAnalysisRuleSet>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|x86' ">
    <OutputPath>bin\x86\Release\</OutputPath>
    <BaseAddress>285212672</BaseAddress>
    <DebugType>
    </DebugType>
    <UseVSHostingProcess>false</UseVSHostingProcess>
    <CodeAnalysisRuleSet>AllRules.ruleset</CodeAnalysisRuleSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)' == 'Debug|x64'">
    <OutputPath>bin\x64\Debug\</OutputPath>
    <BaseAddress>285212672</BaseAddress>
    <CodeAnalysisLogFile>bin\x86\Debug\TestExecServer.exe.CodeAnalysisLog.xml</CodeAnalysisLogFile>
    <UseVSHostingProcess>false</UseVSHostingProcess>
    <CodeAnalysisRuleSet>AllRules.ruleset</CodeAnalysisRuleSet>
    <CodeAnalysisRuleSetDirectories>;C:\Program Files (x86)\Microsoft Visual Studio 10.0\Team Tools\Static Analysis Tools\\Rule Sets</CodeAnalysisRuleSetDirectories>
    <CodeAnalysisIgnoreBuiltInRuleSets>true</CodeAnalysisIgnoreBuiltInRuleSets>
    <CodeAnalysisRuleDirectories>;C:\Program Files (x86)\Microsoft Visual Studio 10.0\Team Tools\Static Analysis Tools\FxCop\\Rules</CodeAnalysisRuleDirectories>
    <CodeAnalysisIgnoreBuiltInRules>true</CodeAnalysisIgnoreBuiltInRules>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)' == 'Release|x64'">
    <OutputPath>bin\x64\Release\</OutputPath>
    <BaseAddress>285212672</BaseAddress>
    <DebugType />
    <CodeAnalysisLogFile>bin\x86\Release\TestExecServer.exe.CodeAnalysisLog.xml</CodeAnalysisLogFile>
    <UseVSHostingProcess>false</UseVSHostingProcess>
    <CodeAnalysisRuleSet>AllRules.ruleset</CodeAnalysisRuleSet>
    <CodeAnalysisRuleSetDirectories>;C:\Program Files (x86)\Microsoft Visual Studio 10.0\Team Tools\Static Analysis Tools\\Rule Sets</CodeAnalysisRuleSetDirectories>
    <CodeAnalysisIgnoreBuiltInRuleSets>true</CodeAnalysisIgnoreBuiltInRuleSets>
    <CodeAnalysisRuleDirectories>;C:\Program Files (x86)\Microsoft Visual Studio 10.0\Team Tools\Static Analysis Tools\FxCop\\Rules</CodeAnalysisRuleDirectories>
    <CodeAnalysisIgnoreBuiltInRules>true</CodeAnalysisIgnoreBuiltInRules>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="..\CommonFiles\GrpcServerBase.cs" Link="GrpcServerBase.cs" />
  </ItemGroup>
  <ItemGroup>
    <Reference Update="System">
      <Name>System</Name>
    </Reference>
    <Reference Update="System.Data">
      <Name>System.Data</Name>
    </Reference>
    <Reference Update="System.Drawing">
      <Name>System.Drawing</Name>
    </Reference>
    <Reference Update="System.Xml">
      <Name>System.XML</Name>
    </Reference>
  </ItemGroup>
  <ItemGroup>
    <Content Include="..\CommonFiles\server_config.json" Link="server_config.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </Content>
    <Content Include="App.ico" />
  </ItemGroup>
  <PropertyGroup />
  <ItemGroup>
    <None Include="..\CommonFiles\certs\client_self_signed_crt.pem" Link="certs\client_self_signed_crt.pem">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\CommonFiles\certs\server.pfx" Link="certs\server.pfx">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\CommonFiles\certs\server_privatekey.pem" Link="certs\server_privatekey.pem">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\CommonFiles\certs\server_self_signed_crt.pem" Link="certs\server_self_signed_crt.pem">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\LoadError.seq" Link="ExampleFiles\LoadError.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\LoopForever.seq" Link="ExampleFiles\LoopForever.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\RunTimeError.seq" Link="ExampleFiles\RunTimeError.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\StepResults.seq" Link="ExampleFiles\StepResults.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\Test.seq" Link="ExampleFiles\Test.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Include="..\ExampleFiles\TraceExecution.seq" Link="ExampleFiles\TraceExecution.seq">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
  </ItemGroup>
  <ItemGroup>
    <PackageReference Include="Grpc.AspNetCore" Version="2.48.0" />
    <PackageReference Include="Grpc.AspNetCore.Web" Version="2.48.0" />
    <PackageReference Include="Microsoft.AspNetCore.Authentication.Certificate" Version="6.0.9" />
    <PackageReference Include="Microsoft.DotNet.UpgradeAssistant.Extensions.Default.Analyzers" Version="0.3.246501">
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.Windows.Compatibility" Version="5.0.2" />
    <PackageReference Include="NationalInstruments.TestStand.Grpc.Server" Version="0.5.0-*" />
  </ItemGroup>
  <ItemGroup>
    <ProjectReference Include="..\..\Grpc.Utilities\Grpc.Utilities.csproj" />
  </ItemGroup>
	<Target Name="PostBuildClean" AfterTargets="Clean">
		<RemoveDir Directories="$(OutDir)" />
	</Target>
</Project>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/TestExecServer.exe.manifest sha256=0aaf876217fc72ad9e827a86c6e9576602d2d93a74a515a06077d53fab945a6f bytes=1007 -->
## FILE: Server/UI/TestExecServer.exe.manifest

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/TestExecServer.exe.manifest`
- sha256: `0aaf876217fc72ad9e827a86c6e9576602d2d93a74a515a06077d53fab945a6f`
- bytes: 1007

````text
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <asmv3:application xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
    </asmv3:windowsSettings>
  </asmv3:application>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
          type="win32"
          name="Microsoft.Windows.Common-Controls"
          version="6.0.0.0"
          processorArchitecture="*"
          publicKeyToken="6595b64144ccf1df"
          language="*"
        />
    </dependentAssembly>
  </dependency>
  <!-- Identify the application security requirements. -->
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
          level="asInvoker"
          uiAccess="False"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/UI/TestExecServer.sln sha256=a1ea0e6d857a7b56dedf57a208116fad2ed9f1f7a6017c4abf2da6677ad5784c bytes=2289 -->
## FILE: Server/UI/TestExecServer.sln

- repository: `ni/grpc-teststand-api`
- source_path: `Server/UI/TestExecServer.sln`
- sha256: `a1ea0e6d857a7b56dedf57a208116fad2ed9f1f7a6017c4abf2da6677ad5784c`
- bytes: 2289

````text
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.2.32616.157
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "TestExecServer", "TestExecServer.csproj", "{A74A634B-152C-488B-9DC9-03116D0DC29C}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "Grpc.Utilities", "..\..\Grpc.Utilities\Grpc.Utilities.csproj", "{DDD59A37-255E-4596-9D60-9E45FC53D9EE}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Debug|x64 = Debug|x64
		Release|Any CPU = Release|Any CPU
		Release|x64 = Release|x64
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|Any CPU.ActiveCfg = Debug|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|Any CPU.Build.0 = Debug|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|x64.ActiveCfg = Debug|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|x64.Build.0 = Debug|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|Any CPU.ActiveCfg = Release|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|Any CPU.Build.0 = Release|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|x64.ActiveCfg = Release|x64
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|x64.Build.0 = Release|x64
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Debug|x64.ActiveCfg = Debug|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Debug|x64.Build.0 = Debug|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Release|Any CPU.Build.0 = Release|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Release|x64.ActiveCfg = Release|Any CPU
		{DDD59A37-255E-4596-9D60-9E45FC53D9EE}.Release|x64.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {A298E105-7F2C-4DF0-B8D0-874DB3329F1B}
	EndGlobalSection
EndGlobal
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/AssemblyInfo.cs sha256=4a8c21c7d6a14e03612a5e4ea2af0e4a0cb3c438cced89f89c5bbdca4e32ed1b bytes=2666 -->
## FILE: Server/WindowsService/AssemblyInfo.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/AssemblyInfo.cs`
- sha256: `4a8c21c7d6a14e03612a5e4ea2af0e4a0cb3c438cced89f89c5bbdca4e32ed1b`
- bytes: 2666

````csharp
using System.Reflection;
using System.Runtime.CompilerServices;
using NationalInstruments.TestStand.Interop.API;

//
// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
//
[assembly: AssemblyTitle(VersionConstants.VersionConstant_Product + " gRPC Service")]
[assembly: AssemblyDescription(VersionConstants.VersionConstant_Product + " gRPC Service")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("[YourCompanyHere]")]
[assembly: AssemblyProduct("[YourProductNameHere]")]
[assembly: AssemblyCopyright("[YourCopyrightHere]")]
[assembly: AssemblyTrademark("[YourTrademarkHere]")]
[assembly: AssemblyCulture("")]		

//
// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Revision and Build Numbers 
// by using the '*' as shown below:

[assembly: AssemblyVersion("1.0.0.0")]

//
// In order to sign your assembly you must specify a key to use. Refer to the 
// Microsoft .NET Framework documentation for more information on assembly signing.
//
// Use the attributes below to control which key is used for signing. 
//
// Notes: 
//   (*) If no key is specified, the assembly is not signed.
//   (*) KeyName refers to a key that has been installed in the Crypto Service
//       Provider (CSP) on your machine. KeyFile refers to a file which contains
//       a key.
//   (*) If the KeyFile and the KeyName values are both specified, the 
//       following processing occurs:
//       (1) If the KeyName can be found in the CSP, that key is used.
//       (2) If the KeyName does not exist and the KeyFile does exist, the key 
//           in the KeyFile is installed into the CSP and used.
//   (*) In order to create a KeyFile, you can use the sn.exe (Strong Name) utility.
//       When specifying the KeyFile, the location of the KeyFile should be
//       relative to the project output directory which is
//       %Project Directory%\obj\<configuration>. For example, if your KeyFile is
//       located in the project directory, you would specify the AssemblyKeyFile 
//       attribute as [assembly: AssemblyKeyFile("..\\..\\mykey.snk")]
//   (*) Delay Signing is an advanced option - see the Microsoft .NET Framework
//       documentation for more information on this.
//
[assembly: AssemblyDelaySign(false)]
[assembly: AssemblyKeyFile("")]
[assembly: AssemblyKeyName("")]
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/GrpcService.cs sha256=3ca35223359ed7272fa501c2ff27105624b21ba564a36c98efb2f54fc4ec07db bytes=1379 -->
## FILE: Server/WindowsService/GrpcService.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/GrpcService.cs`
- sha256: `3ca35223359ed7272fa501c2ff27105624b21ba564a36c98efb2f54fc4ec07db`
- bytes: 1379

````csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using TestStandGrpcApi;

namespace TestExecWindowsService
{
	internal class GrpcService : GrpcServerBase
	{
		public static void Start(string[] args)
		{
			InitializeServerOptions(args);

			IHostBuilder hostBuilder = CreateHostBuilder<GrpcService>(args)
				// This call builds the Windows Service that will run the TestStand gRPC service
				.UseWindowsService(options =>
				{
					string connectionType = UsesHttps ? " [Secure]" : " [Not secure]";
					options.ServiceName = "NI TestStand gRPC Windows Service" + connectionType + ". Listening at port number '" + ServerOptions.Port + "'.";
				});

			ServerHost = hostBuilder.Build();
			ServerHost.Run();
		}

		public GrpcService(IConfiguration configuration) : base(configuration)
		{
		}

		public static void ConfigureServices(IServiceCollection services)
		{
			ConfigureServicesCore(services);

			// This call registers the background service that starts TestStand.
			services.AddHostedService<WindowsService>();
		}

		public static void Configure(IApplicationBuilder app, IWebHostEnvironment webHostEnvironment)
		{
			ConfigureCore(app, webHostEnvironment);
		}
	}
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/MainForm.cs sha256=bd4306aff3fe3a0afc10c3297d97185d38557ace68331b0c44d40cd57c7dbc65 bytes=19115 -->
## FILE: Server/WindowsService/MainForm.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/MainForm.cs`
- sha256: `bd4306aff3fe3a0afc10c3297d97185d38557ace68331b0c44d40cd57c7dbc65`
- bytes: 19115

````csharp
// Note:	This application has a manifest file in the project. This manifest file includes the Microsoft.Windows.Common-Controls which 
//			enables the application to display controls using the XP theme that the operating system selects.
//			The manifest file is specified in the project settings.
//			In order for the manifest file to enable the executable to display with the XP theme:
//			1. The manifest file must have the same name as the executable. For example, if your executable is named MyExecutable.exe, your manifest file is required to have the name MyExecutable.exe.manifest.
//			2. The manifest file must include the Microsoft.Windows.Common-Controls.
//			3. The manifest file must reside in the same directory as the executable.
//			Also note that if you enable the Project Properties>>Debug>>Enable Visual Studio Hosting Process option, the XP theme adaption does not occur when debugging the executable
//			because the Visual Studio environment creates the process and does not allow the manifest file to be embedded into the executable.
using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Runtime.Versioning;
using System.Windows.Forms;
using NationalInstruments.TestStand.Grpc.Net.Server.OO;
using NationalInstruments.TestStand.Interop.API;

// TestStand User Interface Controls
using NationalInstruments.TestStand.Interop.UI;
using NationalInstruments.TestStand.Interop.UI.Ax;

// .net specific functions for use with TestStand APIs (TSUtil)
using NationalInstruments.TestStand.Utility;

namespace TestExecWindowsService
{
	/// <summary>
	/// Summary description for MainForm.
	/// </summary>
	public class MainForm : Form
	{
		private const int WM_QUERYENDSESSION = 0x11;

		private Timer _gcTimer;
		private AxApplicationMgr _axApplicationMgr;
		private AxExecutionViewMgr _axExecutionViewMgr;
		private AxSequenceFileViewMgr _axSequenceFileViewMgr;
		private PreviousServerConfigurationOptions _previousServerOptions;
		private IContainer components;

		// Flag that will be set to true if the user tries to shut down windows
		private bool _sessionEnding = false;
		private bool _calledOnLoad;

		public MainForm()
		{
			// Required for Windows Form Designer support
			InitializeComponent();
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if (disposing)
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
			this._axApplicationMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxApplicationMgr();
			this._gcTimer = new Timer(this.components);
			this._axExecutionViewMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxExecutionViewMgr();
			this._axSequenceFileViewMgr = new NationalInstruments.TestStand.Interop.UI.Ax.AxSequenceFileViewMgr();
			((System.ComponentModel.ISupportInitialize)(this._axApplicationMgr)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this._axExecutionViewMgr)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this._axSequenceFileViewMgr)).BeginInit();
			this.SuspendLayout();
			// 
			// axApplicationMgr
			// 
			this._axApplicationMgr.Location = new System.Drawing.Point(644, 332);
			this._axApplicationMgr.Name = "axApplicationMgr";
			this._axApplicationMgr.OcxState = (AxHost.State)resources.GetObject("axApplicationMgr.OcxState");
			this._axApplicationMgr.Size = new System.Drawing.Size(32, 32);
			this._axApplicationMgr.TabIndex = 16;
			this._axApplicationMgr.DisplaySequenceFile += ApplicationMgr_DisplaySequenceFile;
			this._axApplicationMgr.DisplayExecution += ApplicationMgr_DisplayExecution;
			this._axApplicationMgr.ExitApplication += ApplicationMgr_ExitApplication;
			this._axApplicationMgr.QueryShutdown += AxApplicationMgr_QueryShutdown;
			this._axApplicationMgr.QueryCloseExecution += AxApplicationMgr_QueryCloseExecution;
			this._axApplicationMgr.QueryReloadSequenceFile += AxApplicationMgr_QueryReloadSequenceFile;
			this._axApplicationMgr.ReportError += ApplicationMgr_ReportError;
			// 
			// GCTimer
			// 
			this._gcTimer.Interval = 3000;
			this._gcTimer.Tick += new EventHandler(this.GCTimerTick);
			// 
			// axExecutionViewMgr
			// 
			this._axExecutionViewMgr.Location = new System.Drawing.Point(720, 331);
			this._axExecutionViewMgr.Name = "axExecutionViewMgr";
			this._axExecutionViewMgr.OcxState = (AxHost.State)resources.GetObject("axExecutionViewMgr.OcxState");
			this._axExecutionViewMgr.Size = new System.Drawing.Size(32, 32);
			this._axExecutionViewMgr.TabIndex = 18;
			// 
			// axSequenceFileViewMgr
			// 
			this._axSequenceFileViewMgr.Location = new System.Drawing.Point(682, 331);
			this._axSequenceFileViewMgr.Name = "axSequenceFileViewMgr";
			this._axSequenceFileViewMgr.OcxState = (AxHost.State)resources.GetObject("axSequenceFileViewMgr.OcxState");
			this._axSequenceFileViewMgr.Size = new System.Drawing.Size(32, 32);
			this._axSequenceFileViewMgr.TabIndex = 17;
			// 
			// MainForm
			// 
			this.ClientSize = new System.Drawing.Size(882, 604);
			this.Controls.Add(this._axSequenceFileViewMgr);
			this.Controls.Add(this._axExecutionViewMgr);
			this.Controls.Add(this._axApplicationMgr);
			this.FormBorderStyle = FormBorderStyle.FixedDialog;
			this.MaximizeBox = false;
			this.Name = "MainForm";
			this.StartPosition = FormStartPosition.CenterScreen;
			this.Closing += MainForm_Closing;
			this.Load += MainForm_Load;
			((System.ComponentModel.ISupportInitialize)(this._axApplicationMgr)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this._axExecutionViewMgr)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this._axSequenceFileViewMgr)).EndInit();
			this.ResumeLayout(false);
		}

		#endregion

		protected override void SetVisibleCore(bool value)
		{
			// Don't show the window, but load the form
			if (!_calledOnLoad)
			{
				_calledOnLoad = true;
				OnLoad(EventArgs.Empty);
			}
		}

		private void MainForm_Load(object sender, EventArgs e)
		{			
			try
			{
				// If this UI is running in a CLR other than the one TestStand uses,
				// then it needs its own GCTimer for that version of the CLR. If it's running in the
				// same CLR as TestStand then the engine's gctimer enabled by the ApplicationMgr
				// is sufficient. See the API help for Engine.DotNetGarbageCollectionInterval for more details.
				if (Environment.Version.ToString() != _axApplicationMgr.GetEngine().DotNetCLRVersion)
					_gcTimer.Enabled = true;

				ConfigureServer();

				// make the managers available as named grpc globals
				ConnectionFactory.ServerGlobalScope.ToInstanceId(_axApplicationMgr.GetOcx(), true, "ApplicationMgr");
				ConnectionFactory.ServerGlobalScope.ToInstanceId(_axSequenceFileViewMgr.GetOcx(), true, "SequenceFileViewMgr");
				ConnectionFactory.ServerGlobalScope.ToInstanceId(_axExecutionViewMgr.GetOcx(), true, "ExecutionFileViewMgr");

				_axApplicationMgr.Start();   // start up the TestStand User Interface Components.

				// Enable finding example sequence files in the location of the executable.
				EnableApplicationDirectorySearchPath();
			}
			catch (Exception theException)
			{
				if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
				{
					WriteErrorToEventLog(theException.Message);
				}
				Close();
			}

			if (!string.IsNullOrEmpty(GrpcService.ErrorMessage))
			{
				string message = "Failed to initialize gRPC service with following error(s):\n\n" + GrpcService.ErrorMessage;
				if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
				{
					WriteErrorToEventLog(message);
				}
				Close();
			}
		}

		private void EnableApplicationDirectorySearchPath()
		{
			SearchDirectories searchDirectories = _axApplicationMgr.GetEngine().SearchDirectories;

			foreach (SearchDirectory searchDirectory in searchDirectories)
			{
				if (searchDirectory.Type == SearchDirectoryTypes.SearchDirectoryType_ApplicationDir)
				{
					searchDirectory.Disabled = false;
					break;
				}
			}
		}

		// Configure server to avoid showing popups. This only applies to any popups that TestStand might show
		// when running an execution. It does not prevent popups shown by user code modules.
		private void ConfigureServer()
		{
			StationOptions stationOptions = _axApplicationMgr.GetEngine().StationOptions;

			// First, save current settings of all options that are going to be modified.
			_previousServerOptions = new PreviousServerConfigurationOptions();
			_previousServerOptions._loginOnStart = stationOptions.LoginOnStart;
			_previousServerOptions._enableUserPrivilegeChecking = stationOptions.EnableUserPrivilegeChecking;
			_previousServerOptions._rteOption = stationOptions.RTEOption;
			_previousServerOptions._executingAbortingLimitAction = stationOptions.GetTimeLimitAction(TimeLimitTypes.TimeLimitType_NormalExecution, TimeLimitOperations.TimeLimitOperation_Aborting);
			_previousServerOptions._exitingAbortingTimeLimit = stationOptions.GetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting);
			_previousServerOptions._exitingExecutingTimeLimit = stationOptions.GetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing);
			_previousServerOptions._exitingTerminatingTimeLimit = stationOptions.GetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating);
			_previousServerOptions._exitingAbortingLimitAction = stationOptions.GetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting);
			_previousServerOptions._exitingExecutingLimitAction = stationOptions.GetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing);
			_previousServerOptions._exitingTerminatingLimitAction = stationOptions.GetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating);

			// this is a server, no sense in prompting to log in a local user
			stationOptions.LoginOnStart = false;
			stationOptions.EnableUserPrivilegeChecking = false;

			// Don't show any dialogs when an error occurs
			stationOptions.RTEOption = RTEOptions.RTEOption_Continue;

			// Don't prompt to abort an execution
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_NormalExecution, TimeLimitOperations.TimeLimitOperation_Aborting, TimeLimitActions.TimeLimitAction_KillThreads);

			// Make sure server does not show any dialogs when shutting down.
			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting, 0);
			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing, 0);
			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating, 0);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting, TimeLimitActions.TimeLimitAction_KillThreads);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing, TimeLimitActions.TimeLimitAction_Abort);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating, TimeLimitActions.TimeLimitAction_Abort);
		}

		// Restore all the settings modified service.
		private void RestoreServerSettings()
		{
			StationOptions stationOptions = _axApplicationMgr.GetEngine().StationOptions;

			stationOptions.LoginOnStart = _previousServerOptions._loginOnStart;
			stationOptions.EnableUserPrivilegeChecking = _previousServerOptions._enableUserPrivilegeChecking;
			stationOptions.RTEOption = _previousServerOptions._rteOption;

			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_NormalExecution, TimeLimitOperations.TimeLimitOperation_Aborting, _previousServerOptions._executingAbortingLimitAction);

			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting, _previousServerOptions._exitingAbortingTimeLimit);
			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing, _previousServerOptions._exitingExecutingTimeLimit);
			stationOptions.SetTimeLimit(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating, _previousServerOptions._exitingTerminatingTimeLimit);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Aborting, _previousServerOptions._exitingAbortingLimitAction);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Executing, _previousServerOptions._exitingExecutingLimitAction);
			stationOptions.SetTimeLimitAction(TimeLimitTypes.TimeLimitType_Exiting, TimeLimitOperations.TimeLimitOperation_Terminating, _previousServerOptions._exitingTerminatingLimitAction);
		}

		private void MainForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
		{
			// Don't set e.Cancel to true if windows is shutting down.
			// Doing so would prevent windows from shutting down or logging out.
			if (!_sessionEnding)
			{
				// initiate shutdown and cancel close if shutdown is not complete.  The applicationMgr will
				// send the ExitApplication event when shutdown is complete and we can close then
				if (_axApplicationMgr.Shutdown() == false)
				{
					e.Cancel = true;
				}
			}

			if (!e.Cancel)
            {
				RestoreServerSettings();

				// Since server is shutting down, discard all connections to make sure
				// all objects in those connections are also released.
				ConnectionFactory.DiscardAllConnections();
			}
		}

		protected override void WndProc(ref Message msg)
		{
			// set the sessionEnding flag so I will know the form is closing because the user
			// is trying to shutdown, restart, or logoff windows
			if (msg.Msg == WM_QUERYENDSESSION)
			{
				_sessionEnding = true;
				Close();
			}

			base.WndProc(ref msg);
		}

		// It is now ok to exit, close the form
		private void ApplicationMgr_ExitApplication(object sender, EventArgs e)
		{
			Environment.ExitCode = _axApplicationMgr.ExitCode;
			Close();
			TSHelper.DoSynchronousGCForCOMObjectDestruction();
		}

		private void AxApplicationMgr_QueryShutdown(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_QueryShutdownEvent e)
		{
			e.opt = QueryShutdownOptions.QueryShutdown_Continue;
		}

		private void AxApplicationMgr_QueryReloadSequenceFile(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_QueryReloadSequenceFileEvent e)
		{
			e.opt = QueryReloadSequenceFileOptions.QueryReloadSequenceFile_Cancel;
		}

		private void AxApplicationMgr_QueryCloseExecution(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_QueryCloseExecutionEvent e)
		{
			e.opt = QueryCloseExecutionOptions.QueryCloseExecution_Terminate;
		}

		// ApplicationMgr sends this event to handle any errors it detects.  For example, if a TestStand menu command
		// generates an error, this handler displays it
		private void ApplicationMgr_ReportError(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_ReportErrorEvent e)
		{
			if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
			{
				WriteErrorToEventLog(ErrorMessage.AppendCodeAndDescription(_axApplicationMgr, e.errorMessage, e.errorCode));
			}
		}

		// the ApplicationMgr sends this event to request that the UI display a particular execution
		private void ApplicationMgr_DisplayExecution(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplayExecutionEvent e)
		{
			_axExecutionViewMgr.Execution = e.exec;
		}

		// the ApplicationMgr sends this event to request that the UI display a particular sequence file
		private void ApplicationMgr_DisplaySequenceFile(object sender, NationalInstruments.TestStand.Interop.UI.Ax._ApplicationMgrEvents_DisplaySequenceFileEvent e)
		{
			_axSequenceFileViewMgr.SequenceFile = e.file;
		}

		// Release all objects periodically.  .NET lets COM objects pile up on the managed heap, seemingly even objects you don't know about such
		// as parameters to unhandled ActiveX events.  This timer ensures that all COM objects are released in a timely manner,
		// thus preventing the performance hiccup that could occur when .NET finally decides to collect garbage. Also, this timer
		// ensures that actions triggered by object destruction run in a timely manner. For example: sequence file unload callbacks.
		private void GCTimerTick(object sender, EventArgs e)
		{
			GC.Collect(GC.MaxGeneration, GCCollectionMode.Forced, false); // force .net garbage collection
		}

		[SupportedOSPlatform("windows")]  // Added this to remove warning CA1416
		public static void WriteErrorToEventLog(string textToLog)
		{
			WriteToEventLog(textToLog, EventLogEntryType.Error);
		}

		[SupportedOSPlatform("windows")]  // Added this to remove warning CA1416
		public static void WriteInformationToEventLog(string textToLog)
		{
			WriteToEventLog(textToLog, EventLogEntryType.Information);
		}

		[SupportedOSPlatform("windows")]  // Added this to remove warning CA1416
		private static void WriteToEventLog(string textToLog, EventLogEntryType type)
		{
			const string logSource = "TestStand gRPC Server";

			if (!EventLog.SourceExists(logSource))
			{
				EventLog.CreateEventSource(logSource, "Application");
			}

			EventLog.WriteEntry(logSource, textToLog, type);
		}

		private struct PreviousServerConfigurationOptions
		{
			public bool _loginOnStart;
			public bool _enableUserPrivilegeChecking;

			public RTEOptions _rteOption;

			public TimeLimitActions _executingAbortingLimitAction;

			public double _exitingAbortingTimeLimit;
			public double _exitingExecutingTimeLimit;
			public double _exitingTerminatingTimeLimit;

			public TimeLimitActions _exitingAbortingLimitAction;
			public TimeLimitActions _exitingExecutingLimitAction;
			public TimeLimitActions _exitingTerminatingLimitAction;
		}
	}
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/MainForm.resx sha256=48524dfcb82e344fb818fb6a2af878ef848dcf784990112c608649f42eefe9ce bytes=10475 -->
## FILE: Server/WindowsService/MainForm.resx

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/MainForm.resx`
- sha256: `48524dfcb82e344fb818fb6a2af878ef848dcf784990112c608649f42eefe9ce`
- bytes: 10475

````text
<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="axApplicationMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAA/gAAAAIB
        AAAAAQAAAAAAAAAAAAAAAOkAAAAXAQEAAU8DAABPAwAAAQEBAgAAACYAAABDAEUAbgBnAGkAbgBlAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAADAAAAGAAAAEMAQwBvAG4AZgBpAGcARgBpAGwAZQAAAAEA
        AAAAAgAAAAEAAgAAAFQAAAAlAFQAZQBzAHQAUwB0AGEAbgBkAEwAbwBjAGEAbABBAHAAcABEAGEAdABh
        ACUAXABVAHMAZQByAEkAbgB0AGUAcgBmAGEAYwBlAC4AeABtAGwAAAACAAG4CwAAAAMAAAABAC0AAAAH
        AAAAARAAAAEQAAABAQs=
</value>
  </data>
  <data name="axExecutionViewMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAXAAAAAIB
        AAAAAQAAAAAAAAAAAAAAAEcAAAAZAQEAAU8DAABPAwAAAQIAAAAoAAAAQwBFAHgAZQBEAGkAcwBwAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAABAQAAAAs=
</value>
  </data>
  <data name="axSequenceFileViewMgr.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAXAAAAAIB
        AAAAAQAAAAAAAAAAAAAAAEcAAAAZAQEAAU8DAABPAwAAAQIAAAAoAAAAQwBTAGUAcQBEAGkAcwBwAEIA
        aQBuAGQATQBhAG4AYQBnAGUAcgAAAAEAAAABAQAAAAs=
</value>
  </data>
  <data name="axSequenceView.OcxState" mimetype="application/x-microsoft.net.object.binary.base64">
    <value>
        AAEAAAD/////AQAAAAAAAAAMAgAAAFdTeXN0ZW0uV2luZG93cy5Gb3JtcywgVmVyc2lvbj00LjAuMC4w
        LCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAACFTeXN0
        ZW0uV2luZG93cy5Gb3Jtcy5BeEhvc3QrU3RhdGUBAAAABERhdGEHAgIAAAAJAwAAAA8DAAAAjAUAAAIB
        AAAAAQAAAAAAAAAAAAAAAHcFAAAXAQEAABADAADIAAAAAf//AAD//wAAAAAIAACAgICAAAUAAIDAwMAA
        AgAAAAADUuMLkY/OEZ3jAKoAS7hRAQAAAJABREIBABRNaWNyb3NvZnQgU2FucyBTZXJpZgMAAAAAA1Lj
        C5GPzhGd4wCqAEu4UQEAAACQAURCAQAUTWljcm9zb2Z0IFNhbnMgU2VyaWYEAAAAAANS4wuRj84RneMA
        qgBLuFEBAAAAkAFEQgEAFE1pY3Jvc29mdCBTYW5zIFNlcmlmBQAAAAQAAAAKAAAATgBhAG0AZQAAAAIA
        AAAAAL4AAAABAQAAAAIAAAAAAAIAAAAAAAoAAABOAGEAbQBlAAAAAAAAABgAAABEAGUAcwBjAHIAaQBw
        AHQAaQBvAG4AAAACAAAAAAAiAQAAAQMAAAACAAAAAAACAAAAAAAYAAAARABlAHMAYwByAGkAcAB0AGkA
        bwBuAAAAAAAAAB4AAABFAHgAZQBjAHUAdABpAG8AbgAgAEYAbABvAHcAAAACAAAAAACWAAAAAQQAAAAC
        AAAAAAACAAAAAAAeAAAARQB4AGUAYwB1AHQAaQBvAG4AIABGAGwAbwB3AAAAAAAAAA4AAABTAHQAYQB0
        AHUAcwAAAAIAAAAAAHkAAAABBQAAAAIAAAAAADIDAABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4A
        UgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0APQAgACIAIgAgAD8AIAAtADEAIAA6ACAAKABSAHUA
        bgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0APQAgACIA
        RgBhAGkAbABlAGQAIgAgAHwAfAAgAFIAdQBuAFMAdABhAHQAZQAuAFMAdABlAHAALgBSAGUAcwB1AGwA
        dAAuAFMAdABhAHQAdQBzACAAPQA9ACAAIgBFAHIAcgBvAHIAIgApACAAPwAgAHQAcwBSAGUAZAAgADoA
        IABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQAYQB0AHUAcwAgAD0A
        PQAgACIAUABhAHMAcwBlAGQAIgAgAD8AIAB0AHMARwByAGUAZQBuACAAOgAgAFIAdQBuAFMAdABhAHQA
        ZQAuAFMAdABlAHAALgBSAGUAcwB1AGwAdAAuAFMAdABhAHQAdQBzACAAPQA9ACAAIgBTAGsAaQBwAHAA
        ZQBkACIAIAA/ACAAdABzAEwAaQBnAGgAdABHAHIAYQB5ACAAOgAgACgAUgB1AG4AUwB0AGEAdABlAC4A
        UwB0AGUAcAAuAFIAZQBzAHUAbAB0AC4AUwB0AGEAdAB1AHMAIAA9AD0AIAAiAFIAdQBuAG4AaQBuAGcA
        IgAgAAoAIAB8AHwAIABSAHUAbgBTAHQAYQB0AGUALgBTAHQAZQBwAC4AUgBlAHMAdQBsAHQALgBTAHQA
        YQB0AHUAcwAgAD0APQAgACIATABvAG8AcABpAG4AZwAiACkAIAA/ACAAdABzAE0AYQBnAGUAbgB0AGEA
        IAA6ACAAUgB1AG4AUwB0AGEAdABlAC4AUwB0AGUAcAAuAFIAZQBzAHUAbAB0AC4AUwB0AGEAdAB1AHMA
        IAA9AD0AIAAiAFQAZQByAG0AaQBuAGEAdABlAGQAIgAgAD8AIAB0AHMAQgBsAHUAZQAgADoAIAB0AHMA
        QwB5AGEAbgAAAA4AAABTAHQAYQB0AHUAcwAAAAEAAAABAAIAAAAAAAIAAAAAAAMAAAAAAAAAEAAAAAEA
        AAABAAAAAQAAAP////8DAAAAAwAAAAEBBAAAAAAAAAAB//8/AAAACw==
</value>
  </data>
  <assembly alias="mscorlib" name="mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
  <data name="$this.TrayHeight" type="System.Int32, mscorlib">
    <value>25</value>
  </data>
</root>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/Program.cs sha256=f2fcd40a66350679dff6f031d91d167798893d2ebe1b209660d44d693aae22f1 bytes=232 -->
## FILE: Server/WindowsService/Program.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/Program.cs`
- sha256: `f2fcd40a66350679dff6f031d91d167798893d2ebe1b209660d44d693aae22f1`
- bytes: 232

````csharp
namespace TestExecWindowsService
{
	static class Program
	{
		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		static void Main(string[] args)
		{
			GrpcService.Start(args);
		}
	}
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/Properties/PublishProfiles/gRPCService.pubxml sha256=676d625321d502a8c688f041f64866ef31b07bb2c4a274a6c2e985ff663c68a3 bytes=554 -->
## FILE: Server/WindowsService/Properties/PublishProfiles/gRPCService.pubxml

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/Properties/PublishProfiles/gRPCService.pubxml`
- sha256: `676d625321d502a8c688f041f64866ef31b07bb2c4a274a6c2e985ff663c68a3`
- bytes: 554

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<!--
https://go.microsoft.com/fwlink/?LinkID=208121.
-->
<Project>
  <PropertyGroup>
    <Configuration>Release</Configuration>
    <Platform>Any CPU</Platform>
    <PublishDir>bin\Release\net6.0-windows\Service</PublishDir>
    <PublishProtocol>FileSystem</PublishProtocol>
    <TargetFramework>net6.0-windows</TargetFramework>
    <RuntimeIdentifier>win-x64</RuntimeIdentifier>
    <SelfContained>true</SelfContained>
    <PublishReadyToRun>true</PublishReadyToRun>
  </PropertyGroup>
</Project>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/Properties/Resources.Designer.cs sha256=11f013b601a172c015f433f947bf3a0ce65f5ab2ad9e389a8b0dbbe290f0889e bytes=3250 -->
## FILE: Server/WindowsService/Properties/Resources.Designer.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/Properties/Resources.Designer.cs`
- sha256: `11f013b601a172c015f433f947bf3a0ce65f5ab2ad9e389a8b0dbbe290f0889e`
- bytes: 3250

````csharp
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace TestExecServerService.Properties {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "4.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    internal class Resources {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Resources() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("TestExecServerService.Properties.Resources", typeof(Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        internal static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized resource of type System.Drawing.Icon similar to (Icon).
        /// </summary>
        internal static System.Drawing.Icon App {
            get {
                object obj = ResourceManager.GetObject("App", resourceCulture);
                return ((System.Drawing.Icon)(obj));
            }
        }
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/Properties/Resources.resx sha256=f80165af12cb3668d95f9cdd711418b0b2e68d1fa97f611b12d4268eb0b59ed5 bytes=6181 -->
## FILE: Server/WindowsService/Properties/Resources.resx

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/Properties/Resources.resx`
- sha256: `f80165af12cb3668d95f9cdd711418b0b2e68d1fa97f611b12d4268eb0b59ed5`
- bytes: 6181

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <assembly alias="System.Windows.Forms" name="System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" />
  <data name="App" type="System.Resources.ResXFileRef, System.Windows.Forms">
    <value>..\App.ico;System.Drawing.Icon, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a</value>
  </data>
</root>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/Readme.md sha256=42e7bbeab85a69feccebddb6e514d00607e8740417844ddd18699049aad3f3b2 bytes=3272 -->
## FILE: Server/WindowsService/Readme.md

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/Readme.md`
- sha256: `42e7bbeab85a69feccebddb6e514d00607e8740417844ddd18699049aad3f3b2`
- bytes: 3272

````markdown
# TestStand gRPC Windows Service

This example creates a TestStand gRPC server that runs as a Windows service.

To run the service, you need to first publish it and then install it. You must have .NET installed on the server with `dotnet` available as a command. If you completed the [Prerequisites](../../README.md#Prerequisites) section of the other Readme, this command is available already. Otherwise, install the [.NET SDK](https://dotnet.microsoft.com/en-us/download).

---

## Publishing the Windows Service

Publish the service using one of the following methods:
* Option 1: Open a command prompt in `Examples/Server/WindowsService/` and run the following command:  
`dotnet publish -c Release -r win-x64 --sc -o <Output Directory>`
* Option 2: Publish in Visual Studio
    1. Open `Examples/Server/WindowsService/TestExecWindowsService.sln` in Visual Studio. Open the .sln file. Do not select Open Folder.
    2. In the **Solution Configurations** drop-down menu, select **Release**.
    3. Click **Build>Publish Selection**.
    4. In the **Publish** tab, click **Publish**.
    5. When building completes, in the **Publish** tab, click the **Target location** link to find the executable file `TestExecWindowsService.exe`. Note the location of this file, as you will need it in future steps.
    

For more options for `dotnet publish`, see https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish.

---

## Installing the Windows Service
To install the service, run the following command with administrator privileges:  
`sc.exe create "NI TestStand gRPC Service" binpath= "<file-path-to-TestExecWindowsService.exe> --contentRoot <directory-path-to-TestExecWindowsService.exe>"`

To set the description of the service, run the following command with administrator privileges:  
`sc.exe description "NI TestStand gRPC Service" "Allows remote gRPC clients to run and monitor test sequences."`

Note: The service can take some time to initialize and accept client connections. Any errors that occurred during startup are logged to the Windows Event Log. You can see the log using [Windows Event Viewer](https://learn.microsoft.com/en-us/shows/inside/event-viewer).

---

## Starting the Windows Service

Complete the following steps to start the service:

1. Click **Start**, then type **Services** to open the Services app.
2. Right-click **NI TestStand gRPC Service**, and select **Start**.

You can now connect to the service using the example client. Refer to [Launch the Client and Connect to the Server](../../README.md#launch-the-client-and-connect-to-the-server) and [Example Sequence Files](../../README.md#example-sequence-files) for more information.

---

## Removing the Windows Service

To delete the service, run the following command with administrator privileges:  
`sc.exe delete "NI TestStand gRPC Service"`


---

## See Also

[sc.exe create](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-create)

[Creating a Windows Service using BackgroundService](https://learn.microsoft.com/en-us/dotnet/core/extensions/windows-service)

[Creating a Windows Service with .NET 6](https://csharp.christiannagel.com/2022/03/22/windowsservice-2/)
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/TestExecServerService.exe.manifest sha256=0aaf876217fc72ad9e827a86c6e9576602d2d93a74a515a06077d53fab945a6f bytes=1007 -->
## FILE: Server/WindowsService/TestExecServerService.exe.manifest

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/TestExecServerService.exe.manifest`
- sha256: `0aaf876217fc72ad9e827a86c6e9576602d2d93a74a515a06077d53fab945a6f`
- bytes: 1007

````text
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <asmv3:application xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
    </asmv3:windowsSettings>
  </asmv3:application>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
          type="win32"
          name="Microsoft.Windows.Common-Controls"
          version="6.0.0.0"
          processorArchitecture="*"
          publicKeyToken="6595b64144ccf1df"
          language="*"
        />
    </dependentAssembly>
  </dependency>
  <!-- Identify the application security requirements. -->
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
          level="asInvoker"
          uiAccess="False"/>
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/TestExecWindowsService.csproj sha256=c6b1fa9657a565915a4fbce26db2c97925d3daf7ff9f50d0be81472617d8551f bytes=4020 -->
## FILE: Server/WindowsService/TestExecWindowsService.csproj

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/TestExecWindowsService.csproj`
- sha256: `c6b1fa9657a565915a4fbce26db2c97925d3daf7ff9f50d0be81472617d8551f`
- bytes: 4020

````xml
<Project Sdk="Microsoft.NET.Sdk.Worker">
  <PropertyGroup>
    <TargetFramework>net6.0-windows</TargetFramework>
    <ProjectType>Local</ProjectType>
    <ApplicationIcon>App.ico</ApplicationIcon>
    <AssemblyKeyContainerName>
    </AssemblyKeyContainerName>
    <AssemblyOriginatorKeyFile>
    </AssemblyOriginatorKeyFile>
    <DefaultClientScript>JScript</DefaultClientScript>
    <DefaultHTMLPageLayout>Grid</DefaultHTMLPageLayout>
    <DefaultTargetSchema>IE50</DefaultTargetSchema>
    <DelaySign>false</DelaySign>
    <OutputType>WinExe</OutputType>
    <PublishSingleFile Condition="'$(Configuration)' == 'Release'">true</PublishSingleFile>
    <PlatformTarget>x64</PlatformTarget>
    <RunPostBuildEvent>OnBuildSuccess</RunPostBuildEvent>
    <StartupObject>
    </StartupObject>
    <ApplicationManifest>TestExecServerService.exe.manifest</ApplicationManifest>
    <IsWebBootstrapper>false</IsWebBootstrapper>
    <PublishUrl>publish\</PublishUrl>
    <Install>true</Install>
    <InstallFrom>Disk</InstallFrom>
    <UpdateEnabled>false</UpdateEnabled>
    <UpdateMode>Foreground</UpdateMode>
    <UpdateInterval>7</UpdateInterval>
    <UpdateIntervalUnits>Days</UpdateIntervalUnits>
    <UpdatePeriodically>false</UpdatePeriodically>
    <UpdateRequired>false</UpdateRequired>
    <MapFileExtensions>true</MapFileExtensions>
    <ApplicationRevision>0</ApplicationRevision>
    <ApplicationVersion>1.0.0.%2a</ApplicationVersion>
    <UseApplicationTrust>false</UseApplicationTrust>
    <BootstrapperEnabled>true</BootstrapperEnabled>
    <GenerateAssemblyInfo>false</GenerateAssemblyInfo>
    <UseWindowsForms>true</UseWindowsForms>
    <ImportWindowsDesktopTargets>true</ImportWindowsDesktopTargets>
    <ServerGarbageCollection>true</ServerGarbageCollection>
  </PropertyGroup>
  <ItemGroup>
    <Reference Update="System">
      <Name>System</Name>
    </Reference>
    <Reference Update="System.Data">
      <Name>System.Data</Name>
    </Reference>
    <Reference Update="System.Drawing">
      <Name>System.Drawing</Name>
    </Reference>
    <Reference Update="System.Xml">
      <Name>System.XML</Name>
    </Reference>
  </ItemGroup>
  <ItemGroup>
    <Content Include="App.ico" />
  </ItemGroup>
  <ItemGroup>
    <PackageReference Include="Grpc.AspNetCore" Version="2.48.0" />
    <PackageReference Include="Grpc.AspNetCore.Web" Version="2.48.0" />
    <PackageReference Include="Microsoft.AspNetCore.Authentication.Certificate" Version="6.0.9" />
    <PackageReference Include="Microsoft.DotNet.UpgradeAssistant.Extensions.Default.Analyzers" Version="0.3.246501">
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.Extensions.Hosting.WindowsServices" Version="6.0.1" />
    <PackageReference Include="Microsoft.Windows.Compatibility" Version="5.0.2" />
    <PackageReference Include="NationalInstruments.TestStand.gRPC.Server" Version="0.5.0-*" />
  </ItemGroup>
	<ItemGroup>
		<Compile Include="..\CommonFiles\GrpcServerBase.cs" Link="GrpcServerBase.cs" />
	</ItemGroup>
  <ItemGroup>
	  <Content Include="..\CommonFiles\server_config.json" Link="server_config.json">
		  <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
	  </Content>
  </ItemGroup>
  <ItemGroup>
    <Folder Include="Properties\PublishProfiles\" />
  </ItemGroup>
  <ItemGroup>
    <ProjectReference Include="..\..\Grpc.Utilities\Grpc.Utilities.csproj" />
  </ItemGroup>
  <Target Name="PostBuild" AfterTargets="PostBuildEvent">
	<Exec Command="xcopy /I /Y ..\CommonFiles\certs $(OutDir)\certs&#xD;&#xA;xcopy /I /Y ..\ExampleFiles $(OutDir)" />
  </Target>
  <Target Name="PostBuildPublish" AfterTargets="Publish">
	<Exec Command="xcopy /I /Y ..\CommonFiles\certs $(PublishDir)\certs&#xD;&#xA;xcopy /I /Y ..\ExampleFiles $(PublishDir)" />
  </Target>
  <Target Name="PostBuildClean" AfterTargets="Clean">
	<RemoveDir Directories="$(OutDir)" />
  </Target>
</Project>
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/TestExecWindowsService.sln sha256=e3159e0261c139218466d6323981c2a6aeeada8c84e2279151546c448a8f302e bytes=1651 -->
## FILE: Server/WindowsService/TestExecWindowsService.sln

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/TestExecWindowsService.sln`
- sha256: `e3159e0261c139218466d6323981c2a6aeeada8c84e2279151546c448a8f302e`
- bytes: 1651

````text
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.2.32616.157
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "TestExecWindowsService", "TestExecWindowsService.csproj", "{A74A634B-152C-488B-9DC9-03116D0DC29C}"
EndProject
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "Grpc.Utilities", "..\..\Grpc.Utilities\Grpc.Utilities.csproj", "{F46B9C86-B705-4866-A47E-4826891FEF45}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{A74A634B-152C-488B-9DC9-03116D0DC29C}.Release|Any CPU.Build.0 = Release|Any CPU
		{F46B9C86-B705-4866-A47E-4826891FEF45}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{F46B9C86-B705-4866-A47E-4826891FEF45}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{F46B9C86-B705-4866-A47E-4826891FEF45}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{F46B9C86-B705-4866-A47E-4826891FEF45}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {A298E105-7F2C-4DF0-B8D0-874DB3329F1B}
	EndGlobalSection
EndGlobal
````

<!--NI_OSS_SOURCE repo=grpc-teststand-api path=Server/WindowsService/WindowsService.cs sha256=5b45a97a84860219ac66cf61f694a2510f873ae52fc61d943286768f5a177fba bytes=2810 -->
## FILE: Server/WindowsService/WindowsService.cs

- repository: `ni/grpc-teststand-api`
- source_path: `Server/WindowsService/WindowsService.cs`
- sha256: `5b45a97a84860219ac66cf61f694a2510f873ae52fc61d943286768f5a177fba`
- bytes: 2810

````csharp
using System;
using System.Runtime.InteropServices;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using NationalInstruments.TestStand.Utility;

namespace TestExecWindowsService
{
	public class WindowsService : BackgroundService
	{
		private Thread _staThreadForRunningTSServer;
		private MainForm _serverMainForm;
		private ManualResetEvent _waitForFormToClose;
		private bool _shuttingDown;

		// This method starts the TestStand headless server as a background service.
		// For more information about the method see:
		// https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-7.0&tabs=visual-studio#ihostedservice-interface
		protected override Task ExecuteAsync(CancellationToken stoppingToken)
		{
			_waitForFormToClose = new ManualResetEvent(false);

			_staThreadForRunningTSServer = new Thread(StartTestStand);
			if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
			{
				// MainForm requires an STA thread to run.
				_staThreadForRunningTSServer.SetApartmentState(ApartmentState.STA);
			}
			_staThreadForRunningTSServer.Start();

			return Task.CompletedTask;
		}

		public override Task StopAsync(CancellationToken cancellationToken)
		{
			try
			{
				_shuttingDown = true;

				if (_serverMainForm.Created)
				{
					_serverMainForm.BeginInvoke(_serverMainForm.Close);
					_waitForFormToClose.WaitOne(Timeout.Infinite);
				}
			}
			catch (Exception e)
			{
				if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
				{
					MainForm.WriteErrorToEventLog("Error occurred while stopping service.\nError: " + e.Message);
				}
			}

			return Task.CompletedTask;
		}

		public void StartTestStand(object state)
		{
			_serverMainForm = new MainForm();
			ApplicationWrapper.Run(_serverMainForm);

			// When shutting down the Windows service, the method StopAsync is called. StopAsync shutdowns the
			// TestStand server by calling Close on MainForm. StopAsync then waits for TestStand to finish
			// shutting down. This is done by waiting for the event _waitForFormToClose to be signaled.
			// So, we need to signal _waitForFormToClose here to let StopAsync finish shutting down the service.
			_waitForFormToClose.Set();

			// If an error occurs while starting the service, the MainForm will close without
			// shutting down the gRPC service. When that happens, we need to shutdown the 
			// service here.  We cannot shutdown the service in MainForm because it will result
			// in a deadlock because MainForm will wait for the service to shutdown, but the
			// service cannot shutdown because it is waiting for MainForm to close.
			if (!_shuttingDown)
			{
				GrpcService.Shutdown();
			}
		}
	}
}
````
