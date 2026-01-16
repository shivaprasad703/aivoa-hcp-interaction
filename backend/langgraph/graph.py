class StateGraph:
    def __init__(self, state_type=dict):
        self.nodes = {}
        self.entry = None
        self.finish = None

    def add_node(self, name, func):
        self.nodes[name] = func

    def set_entry_point(self, name):
        self.entry = name

    def set_finish_point(self, name):
        self.finish = name

    def compile(self):
        graph = self

        class CompiledGraph:
            def invoke(self, state):
                return graph.nodes[graph.entry](state)

        return CompiledGraph()
