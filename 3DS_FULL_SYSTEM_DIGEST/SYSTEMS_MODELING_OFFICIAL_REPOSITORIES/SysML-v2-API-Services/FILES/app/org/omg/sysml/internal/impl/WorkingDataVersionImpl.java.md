# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/internal/impl/WorkingDataVersionImpl.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/internal/impl/WorkingDataVersionImpl.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/internal/impl/WorkingDataVersionImpl.java
- source_bytes: 1260
- source_sha256: `67cec97e9b7c4e91afbdcdcf78a49590bea24b7a07e506e622ca9562cb073502`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.internal.impl;

import org.omg.sysml.data.ProjectUsage;
import org.omg.sysml.data.impl.ProjectUsageImpl;
import org.omg.sysml.internal.WorkingDataVersion;
import org.omg.sysml.lifecycle.DataVersion;
import org.omg.sysml.lifecycle.impl.CommitImpl;
import org.omg.sysml.lifecycle.impl.DataVersionImpl;
import org.omg.sysml.record.impl.RecordImpl;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.ManyToOne;

@Entity(name = "WorkingDataVersion")
public class WorkingDataVersionImpl extends RecordImpl implements WorkingDataVersion {

    private ProjectUsage source;
    private DataVersion dataVersion;

    @Override
    @ManyToOne(targetEntity = ProjectUsageImpl.class, fetch = FetchType.LAZY)
    public ProjectUsage getSource() {
        return source;
    }

    @Override
    public void setSource(ProjectUsage source) {
        this.source = source;
    }

    @Override
    @ManyToOne(targetEntity = DataVersionImpl.class, fetch = FetchType.LAZY)
    public DataVersion getDataVersion() {
        return dataVersion;
    }

    @Override
    public void setDataVersion(DataVersion dataVersion) {
        this.dataVersion = dataVersion;
    }
}

````
