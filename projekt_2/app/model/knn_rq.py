class KnnRq:
    def __init__(self, k, threshold, stat_x, stat_y):
        self.k = k
        self.threshold = threshold
        self.stat_x = stat_x
        self.stat_y = stat_y

    @staticmethod
    def from_rq(request):
        return KnnRq(
            stat_x=request.args.get('stat_x'),
            stat_y=request.args.get('stat_y'),
            k=int(request.args.get('k', 3)),
            threshold=float(request.args.get('threshold', 80))
        )
