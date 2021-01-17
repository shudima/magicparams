from magicparams import MagicParams


if __name__ == '__main__':
    params = MagicParams()
    params.param1 = 1
    params.param2 = 2
    params.copy_from_argparser()
    print(params.to_dict())
