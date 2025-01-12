class SortRq:
    def __init__(self, field, order, limit, to_display=None):
        self.field = field
        self.order = order
        self.limit = limit
        self.to_display = to_display

    @staticmethod
    def from_rq(rq):
        limit = rq.args.get('limit', '10')
        limit = int(limit) if limit.isdigit() else 10
        return SortRq(
            field=rq.args.get('field', 'name'),
            order=rq.args.get('order', 'asc'),
            limit=limit,
            to_display=rq.args.get('to_display')
        )
