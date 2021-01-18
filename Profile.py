import networkx as nx
import dynetx as dn
import Model.ModelConfig as mc
import Model.epidemics as ep
from past.builtins import xrange


def make_p_graph_simulation(if_seed, profile, p, a, g):
    model = ep.ProfileModel(g)
    config = mc.Configuration()
    config.add_model_parameter('blocked', p)
    config.add_model_parameter('adopter_rate', a)
    config.add_model_parameter('fraction_infected', if_seed)
    for i in g.nodes():
        config.add_node_configuration("profile", i, profile)
    model.set_initial_status(config)
    iterations = model.iteration_bunch(31)
    trends = model.build_trends(iterations)
    print("Simulation Finished")
    return model, trends