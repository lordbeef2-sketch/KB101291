# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.interactive/src/org/omg/sysml/interactive/VizResult.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.interactive/src/org/omg/sysml/interactive/VizResult.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.interactive/src/org/omg/sysml/interactive/VizResult.java
- source_bytes: 4233
- source_sha256: `b890fcb2c7eeaebe4c96be6d3cfaa00fd7db87a7a7a284d453ce7e219cf1ee93`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2020, 2021 Mgnite Inc.
 * Copyright (c) 2020, 2021 Model Driven Solutions, Inc.
 *    
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 *
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *  Hisashi Miyashita, Mgnite
 *  Ed Seidewitz, MDS
 * 
 *****************************************************************************/
package org.omg.sysml.interactive;

public class VizResult {
    public static enum Kind {
    	EXCEPTION,
        EMPTY,
        PLANTUML,
        TEXT,
        SVG
    }

    public final Kind kind;
    private final String result;
    private final Exception exception;
    
    public static class VizException extends Exception {
		private static final long serialVersionUID = 1L;
		
    	public VizException(String message) {
			super(message);
		}
    }

    public static class UnresolvedException extends VizException {
		private static final long serialVersionUID = 1L;

		public UnresolvedException(String name) {
            super("ERROR:Couldn't resolve reference to Element '" + name + "'\n");
        }
    }

    public boolean hasException() {
        return exception != null;
    }

    public String formatException() {
        return this.exception == null? "":
        	   this.exception instanceof VizException? this.exception.getMessage():
        	   this.exception instanceof IllegalArgumentException? "ERROR:" + this.exception.getMessage():
        	   SysMLInteractiveUtil.formatException(exception);
    }

    public String getPlantUML() {
        switch (kind) {
        case EMPTY:
            return "";
        case PLANTUML:
            return result;
        default:
            return null;
        }
    }

    public String getText() {
        switch (kind) {
        case TEXT:
            return result;
        default:
            return null;
        }
    }

    public String getSVG() {
        switch (kind) {
        case EMPTY:
            return "";
        case SVG:
            return result;
        default:
            return null;
        }
    }

    private VizResult(Kind kind, String result) {
        this.kind = kind;
        this.result = result;
        this.exception = null;
    }

    private VizResult(Exception e) {
    	this.kind = Kind.EXCEPTION;
        this.exception = e;
        this.result = null;
    }

    public static VizResult svgResult(String svg) {
        if (svg == null) return emptyResult();
        return new VizResult(Kind.SVG, svg);
    }

    public static VizResult plantumlResult(String plantuml) {
        if (plantuml == null) return emptyResult();
        return new VizResult(Kind.PLANTUML, plantuml);
    }

    public static VizResult textResult(String text) {
        if (text == null) return emptyResult();
        return new VizResult(Kind.TEXT, text);
    }

    public static VizResult unresolvedResult(String name) {
        return new VizResult(new UnresolvedException(name));
    }
    
    public static VizResult vizExceptionResult(String message) {
    	return new VizResult(new VizException(message));
    }

    public static VizResult emptyResult() {
        return new VizResult(Kind.EMPTY, "");
    }

    public static VizResult exceptionResult(Exception e) {
        return new VizResult(e);
    }
    
    public String toString() {
    	return this.kind == Kind.EXCEPTION? this.formatException():
    		   this.kind + "\n" + this.result;
    }
}


````
