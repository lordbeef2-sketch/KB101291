# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/ISysML.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/ISysML.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/ISysML.java
- source_bytes: 2491
- source_sha256: `f4457a0a8172d47a5af5529aec63eab746fc7428a090a0664347ed90cbd01b89`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML 2 Pilot Implementation
 * Copyright (C) 2020  California Institute of Technology ("Caltech")
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 */

package org.omg.sysml.jupyter.kernel;

import io.github.spencerpark.jupyter.channels.JupyterConnection;
import io.github.spencerpark.jupyter.channels.JupyterSocket;
import io.github.spencerpark.jupyter.kernel.KernelConnectionProperties;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.logging.Level;

public class ISysML {
    public static final String LIBRARY_PATH_KEY = "ISYSML_LIBRARY_PATH";
    public static final String API_BASE_PATH_KEY = "ISYSML_API_BASE_PATH";
    public static final String GRAPHVIZ_PATH_KEY = "ISYSML_GRAPHVIZ_PATH";

    private static volatile SysMLKernel kernel;

    public static void initialize() {
        kernel = new SysMLKernel();
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            throw new IllegalArgumentException("Missing connection file argument");
        }

        initialize();

        Path connectionFile = Paths.get(args[0]);

        if (!Files.isRegularFile(connectionFile))
            throw new IllegalArgumentException("Connection file '" + connectionFile + "' isn't a file.");

        String contents = new String(Files.readAllBytes(connectionFile));

        JupyterSocket.JUPYTER_LOGGER.setLevel(Level.WARNING);

        KernelConnectionProperties connProps = KernelConnectionProperties.parse(contents);
        JupyterConnection connection = new JupyterConnection(connProps);

        kernel.becomeHandlerForConnection(connection);

        connection.connect();
        connection.waitUntilClose();
    }

    public static SysMLKernel getKernelInstance() {
        return kernel;
    }
}

````
