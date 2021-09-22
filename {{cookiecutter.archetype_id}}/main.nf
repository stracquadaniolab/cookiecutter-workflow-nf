// enabling nextflow DSL v2
nextflow.enable.dsl=2

process PrintHelloOnFile {

    publishDir "${params.resultsDir}", pattern: "results.txt", mode: 'copy'

    input:
        path data

    output:
        path 'results.txt'

    """
        fit.py --filename ${data} > results.txt
    """

}

workflow {
    channel.fromPath("${params.inputFile}") | PrintHelloOnFile
}

