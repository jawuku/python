{
  description = "Python 3.12 development shell";

  inputs = {
    # pin to stable nixpkgs
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    # helper to write cross-system flakes (Linux/macOS and x86_64/aarch64)
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # import your pinned nixpkgs for this system
        pkgs = import nixpkgs { inherit system; };
        # build a Python 3.12 Env with your exact packages
        pythonEnv = pkgs.python312.withPackages (ps: with ps; [
          sympy
          seaborn
          scikit-learn
          gmpy2
          mpmath
          statsmodels
          requests
          pyyaml
          pycountry
          beautifulsoup4
          jupyter
          yfinance
          tensorflowWithoutCuda
          torchWithoutCuda
        ]);
      in {
        # this is the equivalent of mkShell { … }
        devShells.default = pkgs.mkShell {
          buildInputs = [ pythonEnv ];
          shellHook  = ''
            echo
            echo "-~= You are now in the Nix Python 3.12 shell =~-"
          '';
        };
      }
    );
}
