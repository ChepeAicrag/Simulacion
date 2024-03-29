import networkx as nx 
import dynetx as dn
import Model.ModelConfig as mc
import Model.epidemics as ep
from past.builtins import xrange

def make_pt_graph_simulation(if_seed, profile, threshold, p, a, g):    
    #model = ep.KerteszThresholdModel(dg)
    model = ep.ProfileThresholdModel(g)
    #model = dm.DynProfileThresholdModel(dg)
    config = mc.Configuration()
    config.add_model_parameter('percentage_blocked', p)
    config.add_model_parameter('adopter_rate', a)
    config.add_model_parameter('fraction_infected', if_seed)
    for i in g.nodes():
        config.add_node_configuration("threshold", i, threshold)
        config.add_node_configuration("profile", i, profile)
    model.set_initial_status(config)
    iterations = model.iteration_bunch(30)
    trends = model.build_trends(iterations)
    print("Simulation Finished")
    return model, trends, iterations