process Hello {

    publishDir "${params.resultsDir}", pattern: "results.txt", mode: 'copy'

    input:
        path data

    output:
        path 'results.txt'

    """
        cat ${data} > results.txt
    """

}