{
  description = "A development shell for Manim and Manim Slides with Python 3.13";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux.default =
      let
        pkgs = nixpkgs.legacyPackages.x86_64-linux;
      in
      pkgs.mkShell {
        name = "manim-dev-shell";

        buildInputs = with pkgs; [
          python313Packages.manim
          python313Packages.manim-slides
          texliveFull
        ];

        shellHook = ''
            export PS1="\[\033[01;32m\](manim-dev)\[\033[00m\] \w \$ "
            export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH"
        '';
      };
  };
}
