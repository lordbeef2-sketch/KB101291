# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/util/UUIDDigest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/util/UUIDDigest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/util/UUIDDigest.java
- source_bytes: 3173
- source_sha256: `629d1744f1cf662715f0b30d70153dc37a73940e713e4323caa6e66426ac6c99`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2023 Mgnite Inc.
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
 *  Hisashi Miyashita
 * 
 *****************************************************************************/

package org.omg.sysml.util;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.UUID;

public class UUIDDigest {
	private final MessageDigest md;

	private final long versionMask;
    private static final int VERSION_BIT = 12;
    private static final long MSB_MASK = -1L ^ (0x0F << VERSION_BIT);
    
	private static byte[] makeNamespaceBytes(UUID ns) {
		ByteBuffer buf = ByteBuffer.allocate(16);
		buf.putLong(ns.getMostSignificantBits());
		buf.putLong(ns.getLeastSignificantBits());
		return buf.array();		
	}
    
	public UUID hash(UUID ns, String str) {
		byte[] nsBytes = makeNamespaceBytes(ns);
		byte[] bytes = str.getBytes(StandardCharsets.UTF_8);
		if (md == null) {
			ByteBuffer bb = ByteBuffer.allocate(16 + bytes.length);
            bb.put(nsBytes);
            bb.put(bytes);
			return UUID.nameUUIDFromBytes(bb.array());
		} else {
            md.reset();
            md.update(nsBytes);
            md.update(bytes);

            ByteBuffer bb = ByteBuffer.wrap(md.digest());
            long msb = (bb.getLong() & MSB_MASK) | versionMask;
            long lsb = (bb.getLong() & 0x3fffffffffffffffL) | 0x8000000000000000L;

            return new UUID(msb, lsb);
        }
	}
	
	public UUIDDigest(int version, String algorithm) {
		this.versionMask = (version & 0x0F) << VERSION_BIT;
		try {
			this.md = MessageDigest.getInstance(algorithm);
		} catch (NoSuchAlgorithmException e) {
			throw new IllegalArgumentException("Hash algorithm: " + algorithm + " could not be used");
		}
	}
	
	public UUIDDigest() {
		this.versionMask = 0;
		this.md = null;
	}

    public static void main(String[] args) {
        UUIDDigest[] dds = { new UUIDDigest(), new UUIDDigest(3, "MD5"), new UUIDDigest(3, "SHA-1"), new UUIDDigest(5, "SHA-1") };
        
        UUID ns = UUID.randomUUID();
        
        System.out.println("Namespace UUID: " + ns);
        for (String arg : args) {
            for (UUIDDigest dd : dds) {
                System.out.println(arg + " -> " + dd.hash(ns, arg));
            }
        }
    }
}

````
