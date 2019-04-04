import argparse

from reveal.decoder import DataTransformation
from reveal.handler import B32, B64, HexEnc, Num2Char, UrlEncode, Jwt

__version__ = "1.0.0"

WELCOME = """
  _______    _______  ___      ___  _______       __      ___       
 /"      \  /"     "||"  \    /"  |/"     "|     /""\    |"  |      
|:        |(: ______) \   \  //  /(: ______)    /    \   ||  |      
|_____/   ) \/    |    \\  \/. ./  \/    |     /' /\  \  |:  |      
 //      /  // ___)_    \.    //   // ___)_   //  __'  \  \  |___   
|:  __   \ (:      "|    \\   /   (:      "| /   /  \\  \( \_|:  \  
|__|  \___) \_______)     \__/     \_______)(___/    \___)\_______) 
                                                                    v:%s"""


def print_result(nodes, show_path=True):
    def __print_result(node, path):
        if node.handler is not None:
            path.append(node.handler.name)

        if node.child:
            for itm in node.child:
                __print_result(itm, path)
            return

        if show_path:
            res = "%s = %s" % (" -> ".join(path), node.data)
            print(res)
            print("Encode with: %s" % ",".join(path[::-1]))
        else:
            print(node.data, end="\r\n\r\n")

    return __print_result(nodes, [])


def main():
    parser = argparse.ArgumentParser(description="Detect and decode encoded strings")
    parser.add_argument("--encode", help="Encode string with selected encoders", type=str, metavar="<enc1,enc2,...>")
    parser.add_argument("--limit", help="Maximum deep of decoding recursion", type=int, default=24)
    parser.add_argument("--quiet", help="Print output(s) ONLY.", action="store_true")
    parser.add_argument("string", help="input string")
    args = parser.parse_args()

    dt = DataTransformation()
    dt.add_handler(B32())
    dt.add_handler(B64())
    dt.add_handler(HexEnc())
    dt.add_handler(Num2Char())
    dt.add_handler(UrlEncode())
    dt.add_handler(Jwt())

    if not args.quiet:
        print(WELCOME % __version__, end="\n\n")
        print("Available handlers:")
        tblk = max([len(handler[0]) for handler in dt.available_decoders()])
        for handler in dt.available_decoders():
            print("\t- %s\t%s" % (handler[0] + " " * (tblk - len(handler[0])), handler[1]))
        print()

    if args.encode is not None:
        print(dt.encode(args.string, args.encode.split(",")), end="")
        return 0

    print_result(dt.decode(args.string, args.limit), not args.quiet)
    return 0
