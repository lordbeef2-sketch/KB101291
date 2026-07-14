# LEGACY SOURCE RECORD: References/PLUGIN_SKELETON.java.txt

<!--LEGACY_SOURCE path=References/PLUGIN_SKELETON.java.txt sha256=9ed5ffd48c9a69dca8660867eed34da5702fb7d889840e89c0adca2eba2cf528 bytes=939 -->

- original_path: `References/PLUGIN_SKELETON.java.txt`
- original_sha256: `9ed5ffd48c9a69dca8660867eed34da5702fb7d889840e89c0adca2eba2cf528`
- original_bytes: 939

````text
package example;

import com.nomagic.magicdraw.actions.MDAction;
import com.nomagic.magicdraw.core.Application;
import com.nomagic.magicdraw.plugins.Plugin;

import javax.swing.*;
import java.awt.event.ActionEvent;

public class ExamplePlugin extends Plugin {
    @Override
    public void init() {
        Application.getInstance().getGUILog().log("[ExamplePlugin] initialized");
        // Register actions/configurators here in a real plugin.
    }

    @Override
    public boolean close() {
        return true;
    }

    @Override
    public boolean isSupported() {
        return true;
    }

    public static class ExampleAction extends MDAction {
        public ExampleAction() {
            super("EXAMPLE_ACTION", "Example Action", null, null);
        }

        @Override
        public void actionPerformed(ActionEvent event) {
            JOptionPane.showMessageDialog(null, "Example action executed.");
        }
    }
}
````
