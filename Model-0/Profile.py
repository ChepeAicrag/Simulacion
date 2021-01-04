import networkx as nx
import dynetx as dn
import ndlib.models.ModelConfig as mc
import ndlib.models.dynamic as dm
import ndlib.models.epidemics as ep
from past.builtins import xrange


def make_p_graph_simulation(if_seed, profile, p, a, g):
    # if ds == 1: 
    #     g = nx.barabasi_albert_graph(63392, 13) 
    # elif ds == 2:
    #     g = nx.erdos_renyi_graph(n = 63392, p = 0.0004) 
    # else:
    #     g = nx.watts_strogatz_graph(63392, 13, 0.01) 
    model = ep.ProfileModel(g)
    config = mc.Configuration()
    config.add_model_parameter('blocked', p)
    config.add_model_parameter('adopter_rate', a)
    config.add_model_parameter('fraction_infected', if_seed)
    for i in g.nodes():
        config.add_node_configuration("profile", i, profile)
    model.set_initial_status(config)
    iterations = model.iteration_bunch(30)
    trends = model.build_trends(iterations)
    print("Simulation Finished")
    return model, trends

    #     dg = dn.DynGraph()
    # for t in xrange(1):
    #     if ds == 1: 
    #         g = nx.barabasi_albert_graph(63392, 13) 
    #     elif ds == 2:
    #         g = nx.erdos_renyi_graph(n = 63392, p = 0.0004) 
    #     else:
    #         g = nx.watts_strogatz_graph(63392, 13, 0.01) 
    #     dg.add_interactions_from(g.edges(), t)
    # model = dm.DynProfileModel(dg)
    # config = mc.Configuration()
    # config.add_model_parameter('blocked', p)
    # config.add_model_parameter('adopter_rate', a)
    # config.add_model_parameter('fraction_infected', if_seed)
    # # Setting nodes parameters
    # for i in g.nodes():
    #     config.add_node_configuration("profile", i, profile)
    # model.set_initial_status(config)
    # # Simulate snapshot based execution
    # iterations = model.execute_snapshots()
    # trends = model.build_trends(iterations)
    # print("Simulation Finished")
    # return model, trends