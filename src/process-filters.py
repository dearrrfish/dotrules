from os import path

script_path = path.dirname(path.realpath(__file__))
filter_files = [
    "../modules/divine_engine/Quantumult/X/Filter/Advertising.list",
    "../modules/divine_engine/Quantumult/X/Filter/Hijacking.list",
    "../modules/lhie1/Quantumult/QuantumultX.conf",
    "../modules/nobyda/QuantumultX/AdRule.list",
]

output_rejects = "../dist/QuantumultX/Filter/Rejects.list"

rejects = set()


def main():
    for file in filter_files:
        with open(path.join(script_path, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line or line.startswith("/") or line.startswith("#"):
                    continue
                parts = line.split(",")
                if len(parts) < 3:
                    continue
                mode, uri, rule = parts[:3]
                if rule == "REJECT":
                    if mode == "DOMAIN":
                        mode = "DOMAIN-SUFFIX"
                    rejects.add(",".join([mode, uri, rule]))

    list_rejects = sorted(list(rejects), key=lambda x: x.split(",")[1])
    print("Writing %d reject rules to file..." % len(list_rejects))

    with open(
        path.join(script_path, output_rejects), mode="wt", encoding="utf-8"
    ) as out_rejects:
        out_rejects.write("\n".join(list_rejects))


if __name__ == "__main__":
    main()

