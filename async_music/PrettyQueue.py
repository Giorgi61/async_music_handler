import queue


class PrettyQueue(queue.Queue):

    def __str__(self):
        data_lst = [i for i in self.queue]
        return str(data_lst)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.queue)