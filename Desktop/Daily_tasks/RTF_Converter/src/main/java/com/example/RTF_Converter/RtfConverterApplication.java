package com.example.RTF_Converter;

import com.documents4j.api.DocumentType;
import com.documents4j.api.IConverter;

import javax.swing.text.BadLocationException;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import com.documents4j.job.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class RtfConverterApplication{

	public static void main(String[] args) throws IOException, BadLocationException, ExecutionException, InterruptedException {

		InputStream in = new BufferedInputStream(new FileInputStream(System.getProperty("user.dir") + File.separator +"sample.rtf"));
		ByteArrayOutputStream bo = new ByteArrayOutputStream();
		IConverter converter = LocalConverter.builder()
				.baseFolder(new File(System.getProperty("user.dir") + File.separator ))
				.workerPool(20, 25, 2, TimeUnit.SECONDS)
				.processTimeout(5, TimeUnit.SECONDS)
				.build();
		Future<Boolean> conversion = converter
				.convert(in).as(DocumentType.RTF)
				.to(bo).as(DocumentType.PDF)
				.prioritizeWith(1000) // optional
				.schedule();
		conversion.get();
		try (OutputStream outputStream = new FileOutputStream("out.pdf")) {
			bo.writeTo(outputStream);
		}
		in.close();
		bo.close();
	}

}
