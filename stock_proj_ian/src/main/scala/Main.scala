package org.ian.stock

import org.apache.spark.SparkConf
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.functions.to_date
import org.apache.spark.sql.types.{DateType, IntegerType, StringType, StructField, StructType}
import scala.io.Source

import java.io.{File, FileWriter, BufferedWriter}

import scalaj.http.{Http, HttpResponse}


object Main {
  def main(args: Array[String]): Unit = {
    val filename = ".env"



    // Open the file and read its content
    val bufferedSource = Source.fromFile(filename)
    // Read lines from the file
    val lines = bufferedSource.getLines().toList
    // Close the file
    bufferedSource.close()
    //println(s"interpolaiting ${lines(0)} in a string")
    val url = s"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=INTC&outputsize=full&apikey=${lines(0)}"
    val response: HttpResponse[String] = Http(url).asString

    // Check the response status code and body
    println(s"Response Code: ${response.code}")
    println(s"${response.body}")

    val filePath = "data/INTC.json"
    val content = response.body

    val file = new File(filePath)
    val bw = new BufferedWriter(new FileWriter(file))

    try {
      bw.write(content)
    } finally {
      bw.close()
    }

  }
}