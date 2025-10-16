#!/bin/bash

# Script to export all PlantUML diagrams to specified format
# Usage: ./export-diagrams.sh [-png|-svg|-pdf]
# Default: SVG

# Default format
FORMAT="svg"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -png)
            FORMAT="png"
            shift
            ;;
        -svg)
            FORMAT="svg"
            shift
            ;;
        -pdf)
            FORMAT="pdf"
            shift
            ;;
        -jpeg)
            FORMAT="jpeg"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: ./export-diagrams.sh [-png|-svg|-pdf|-jpeg]"
            exit 1
            ;;
    esac
done

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$SCRIPT_DIR/docs/diagrams/src"
OUT_DIR="$SCRIPT_DIR/docs/diagrams/out"
JAR_FILE="$SCRIPT_DIR/plantuml.jar"

# Check if plantuml.jar exists
if [ ! -f "$JAR_FILE" ]; then
    echo "Error: plantuml.jar not found at $JAR_FILE"
    exit 1
fi

# Check if source directory exists
if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory not found at $SRC_DIR"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUT_DIR"

echo "========================================"
echo "Exporting PlantUML Diagrams"
echo "========================================"
echo "Format: $FORMAT"
echo "Source: $SRC_DIR"
echo "Output: $OUT_DIR"
echo "========================================"
echo ""

# Count diagram files
DIAGRAM_COUNT=$(find "$SRC_DIR" -type f \( -name "*.puml" -o -name "*.plantuml" -o -name "*.uml" \) | wc -l | tr -d ' ')

if [ "$DIAGRAM_COUNT" -eq 0 ]; then
    echo "No diagram files found in $SRC_DIR"
    exit 0
fi

echo "Found $DIAGRAM_COUNT diagram file(s)"
echo ""

# Export diagrams (using source filename)
# PlantUML -o expects relative path from input files
cd "$SRC_DIR" || exit 1

for file in *.puml *.plantuml *.uml; do
    if [ -f "$file" ]; then
        echo "Exporting: $file"
        
        # Get base filename without extension
        basename="${file%.*}"
        
        # Export diagram
        java -jar "$JAR_FILE" -t"$FORMAT" -o "../out" "$file"
        
        # Find the generated file and rename it to match source filename
        # PlantUML generates files based on @startuml name, so we need to find and rename
        latest_file=$(ls -t "../out/"*."$FORMAT" 2>/dev/null | head -n 1)
        if [ -n "$latest_file" ]; then
            target_file="../out/${basename}.${FORMAT}"
            # Only rename if it's not already the correct name
            if [ "$latest_file" != "$target_file" ]; then
                mv "$latest_file" "$target_file" 2>/dev/null || true
            fi
        fi
    fi
done

cd "$SCRIPT_DIR" || exit 1

# Check if export was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "✓ Successfully exported all diagrams!"
    echo "  Format: .$FORMAT"
    echo "  Location: $OUT_DIR"
    echo "========================================"
else
    echo ""
    echo "========================================"
    echo "✗ Export failed!"
    echo "========================================"
    exit 1
fi

