import argparse


def setupParser():
    parser = argparse.ArgumentParser(
        description="Run the Crank-Nicolson simulation for the Gross-Pitaevskii equation",
        epilog="This is for a physics' final degree project at the University of Barcelona",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Setup logging level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
    )

    parser.add_argument(
        "-i",
        "--input",
        help="Python file with the wave function and potential functions",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file for the simulation (.npy)",
        type=str,
        required=False,
        default=None,
    )

    parser.add_argument(
        "-cn",
        "--crank-nicolson",
        help="Python file with the Crank-Nicolson module",
        type=str,
        required=False,
        default=None,
        dest="CNmodule",
    )

    parser.add_argument(
        "-sp",
        "--show-parts",
        help="Show imaginary and real parts of the wave function",
        action="store_true",
        dest="showParts",
    )

    parser.add_argument(
        "-inan",
        "--ignore-nan",
        help="Ignore NaN values in the simulation",
        action="store_true",
        dest="ignoreNan",
    )

    parser.add_argument(
        "-oc",
        "--override-constants",
        help="Override the constants with the provided values (provided as a list of key=value pairs)",
        type=str,
        nargs="+",
        dest="overrideConstants",
    )

    return parser.parse_args()
