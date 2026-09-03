import argparse
from app.recon import recon
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target_ip", help="IP цели для сканирования")
    args = parser.parse_args()
    # дальше значение доступно как args.target_ip

    print(recon(args.target_ip))
