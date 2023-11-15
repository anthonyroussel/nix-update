{ lib, stdenv, fetchurl, nix-update-script }:

stdenv.mkDerivation rec {
  pname = "jetty";
  version = "12.0.2";

  src = fetchurl {
    url = "mirror://maven/org/eclipse/jetty/jetty-home/${version}/jetty-home-${version}.tar.gz";
    hash = "sha256-DtlHTXjbr31RmK6ycDdiWOL7jIpbWNh0la90OnOhzvM=";
  };
}
