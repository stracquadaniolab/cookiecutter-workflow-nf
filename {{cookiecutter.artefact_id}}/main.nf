// enabling nextflow DSL v2
nextflow.enable.dsl=2

process PrintHelloOnFile {

    publishDir "${params.resultsDir}", pattern: "hello.txt", mode: 'copy'

    input:
        path data

    output:
        path 'hello.txt'

    """
        main.py > hello.txt
        cat ${data} >> hello.txt
    """

}

workflow {
    channel.fromPath("${params.inputFile}") | PrintHelloOnFile
}

