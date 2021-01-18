from lib.actions import BaseAction


class GetAction(BaseAction):
    def run(self, table, query, request_params):
        s = self.client
        r = s.query(table=table, query=query, request_params=request_params)  # pylint: disable=no-member
        response = r.get_all()  # pylint: disable=no-member
        output = []
        for each_item in response:
            output.append(each_item)
        return output
