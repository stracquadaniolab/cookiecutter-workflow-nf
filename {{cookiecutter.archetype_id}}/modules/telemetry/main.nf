process TELEMETRY {

    publishDir "${params.resultsDir}", pattern: "run_info.txt", mode: 'copy'

    input:
        path data

    output:
        path 'results.txt'

    """
        cat ${data} > results.txt
    """

}