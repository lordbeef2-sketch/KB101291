# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/internal/WorkingDataVersion.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/internal/WorkingDataVersion.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/internal/WorkingDataVersion.java
- source_bytes: 384
- source_sha256: `6950fc9b567121061a44520a365746ef835793e23bc015783a1fae3cab0596ab`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal;

import org.omg.sysml.data.ProjectUsage;
import org.omg.sysml.lifecycle.DataVersion;
import org.omg.sysml.record.Record;

public interface WorkingDataVersion extends Record {

    ProjectUsage getSource();

    void setSource(ProjectUsage commit);

    DataVersion getDataVersion();

    void setDataVersion(DataVersion dataVersion);
}

````
