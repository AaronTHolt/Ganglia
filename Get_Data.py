#Test Cases
#Get data from txt file assuming slurm sacct was run and piped into txt file
from Utility import *

def get_data(jobid, debug):
    # Data from job 660771
    with open('test_cases/jobs/{j}.txt'.format(j=jobid), 'r') as f:
        data = f.read()
    f.close()

    t1, t2, node_names, cluster_names = parse_job_file(data)

    #convert cluster names to match directory names in rrd
    cluster_names = convert_cluster_names(cluster_names)

    # Expand nodes if necessary and flatten nested lists
    node_names = expand_node_list(node_names)
    
    # Use 4 month window for debugging
    if debug:
        t1 = '2015-01-13T10:21:00'
        t2 = '2015-05-14T09:44:02'

    start = convert_enddate_to_seconds(t1)
    stop = convert_enddate_to_seconds(t2)
    # print start, stop

    return start, stop, cluster_names, node_names