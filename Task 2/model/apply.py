import argparse
from solution import get_model, predict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-data_path', default = '../data')
    parser.add_argument('-result_path', default = '../result/process_results.json')   
    parser.add_argument('-device', default = 'cpu')
    parser.add_argument('-model_path', default = 'eff_9_0.0573.pt')
    parser.add_argument('-cls_thr', default = 0.4, type=float)

    args = parser.parse_args()
    model, device = get_model(args.model_path, args.device)
    predict(model, args.data_path, args.result_path, args.cls_thr, device)