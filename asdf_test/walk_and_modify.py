from asdf.treeutil import walk_and_modify

tree = {
    "a": {"aa": 1, "ab": 3},
    "b": 6,
    "c": {"ca": 5, "cb": 7, "cc": {"cca": 3, "ccb": 8, "ccc": 9}, "d": 2},
}


def callback(node, json_id):
    if isinstance(node, int) and node == 3:
        print(f"json id: {json_id} / node: {node} -> -5")
        return -5
    print(f"json id: {json_id} / node: {node}")
    return node


walk_and_modify(tree, callback, postorder=False)
