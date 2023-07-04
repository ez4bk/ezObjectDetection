class TableResult:
    def __init__(self):
        self.results = {
            # 'example': {'name': 'example', 'frame_count': 1, 'avg_conf': 0.80, 'conf_sum': 0.80}
        }

    def append(self, name, conf):
        if self.results.get(name):
            res = self.results[name]
            res['frame_count'] += 1
            res['conf_sum'] = round((res['conf_sum'] + conf), 2)
            res['avg_conf'] = round((res['conf_sum'] / res['frame_count']), 2)
        else:
            res = {
                'name': name,
                'frame_count': 1,
                'avg_conf': conf,
                'conf_sum': conf
            }
            self.results[name] = res

    def reset_attr(self, name):
        if self.results.get(name):
            self.results[name] = {
                'name': name,
                'frame_count': 0,
                'avg_conf': 0,
                'conf_sum': 0
            }
            return True
        return False

    def to_list(self):
        return list(self.results.values())


