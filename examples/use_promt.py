from magicparams import MagicParams

if __name__ == '__main__':
    params = MagicParams(param1=1, on_missing_param='promt')
    print('param1:', params.param1)
    print('param2:', params.param2)