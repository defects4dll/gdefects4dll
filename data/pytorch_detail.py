torch_61345 = {"container_id": "gdefects4dll-rebug", "image_id": "defects4dll/pytorch:10.2-7"}

pytorch_dict = {
    "torch-61345": torch_61345,
    "torch-61754": {}
}


def get_dict(bugId):
    return pytorch_dict.get(bugId)
