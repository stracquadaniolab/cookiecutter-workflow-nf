process PrintHelloOnFile {

    publishDir "${params.resultsDir}", pattern: "results.txt", mode: 'copy'

    input:
        path data

    output:
        path 'results.txt'

    """
        fit.py ${data} > results.txt
    """

}

workflow {
    channel.fromPath("${params.inputFile}") | PrintHelloOnFile
}

