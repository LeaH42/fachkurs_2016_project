class Process(object):
    """
    Parent for all cellular processes.
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

        self.enzyme_ids = []
        self.substrate_ids = []

    def set_states(self, substrate_ids, enzyme_ids):
        self.enzyme_ids = enzyme_ids
        self.substrate_ids = substrate_ids

    def update(self, model):
        """
        Has to be implemented by child class.
        """
        pass
