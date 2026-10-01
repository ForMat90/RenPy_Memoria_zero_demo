#!/bin/bash
SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  case "$SOURCE" in
    /*) ;;
    *) SOURCE="$DIR/$SOURCE" ;;
  esac
done
cd "$(cd -P "$(dirname "$SOURCE")" && pwd)" || exit 1

if [ ! -f "./renpy-sdk/renpy.sh" ]; then
  echo
  echo "Questo file deve restare dentro la cartella Memoria_zero_demo,"
  echo "insieme alle cartelle game e renpy-sdk."
  echo
  echo "Non spostarlo fuori dalla cartella. Se lo vuoi sulla Scrivania:"
  echo "tasto destro sul file, Crea alias, e sposta solo l'alias."
  echo
  read -n 1 -s -r -p "Premi un tasto per continuare..."
  echo
  exit 1
fi

chmod +x "./renpy-sdk/renpy.sh" \
  "./renpy-sdk/lib/py3-mac-universal/renpy" \
  "./renpy-sdk/lib/py3-mac-universal/python" \
  "./renpy-sdk/lib/py3-mac-universal/pythonw"

exec "./renpy-sdk/renpy.sh" "$(pwd)"
