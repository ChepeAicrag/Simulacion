import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.utils import multi_runs
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend

def test01():
    g = nx.erdos_renyi_graph(1000, 0.1)
    model1 = ep.SIRModel(g)
    config = mc.Configuration()
    config.add_model_parameter('beta', 0.001)
    config.add_model_parameter('gamma', 0.01)
    model1.set_initial_status(config)
    infection_sets = [(1, 2, 3, 4, 5), (3, 23, 22, 54, 2) ]
    trends = multi_runs(model1, execution_number=2, iteration_number=100, infection_sets=infection_sets, nprocesses=4)
    viz = DiffusionTrend(model1, trends)
    viz.plot(filename=None)


def make_pt_graph_simulation(if_seed, profile, threshold, p, a, ds = 1):    
    if ds == 1: 
        dg = nx.barabasi_albert_graph(63392, 13) 
    elif ds == 2:
        dg = nx.erdos_renyi_graph(n = 63392, p = 0.0004) 
    else:
        dg = nx.watts_strogatz_graph(63392, 13, 0.01)     
    #model = ep.KerteszThresholdModel(dg)
    model = ep.ProfileThresholdModel(dg)
    #model = dm.DynProfileThresholdModel(dg)
    config = mc.Configuration()
    config.add_model_parameter('percentage_blocked', p)
    config.add_model_parameter('adopter_rate', a)
    config.add_model_parameter('fraction_infected', if_seed)
    for i in dg.nodes():
        config.add_node_configuration("threshold", i, threshold)
        config.add_node_configuration("profile", i, profile)
    model.set_initial_status(config)
    iterations = model.iteration_bunch(30)
    trends = model.build_trends(iterations)
    print("Simulation Finished")
    return model, trends, iterations
    
if __name__ == "__main__":
    test01()