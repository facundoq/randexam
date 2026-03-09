#!/bin/bash
VERSION="v$(grep -m 1 '^version =' pyproject.toml | cut -d '"' -f 2)"

echo "Commiting $VERSION..."
echo "Adding all files to git commit..."
git add .
git status
echo "Creating and pusing commit..."
git commit -m "$VERSION" && git push
echo "Tagging commit..."
git tag "$VERSION" && git push --tags