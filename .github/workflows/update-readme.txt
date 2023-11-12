# name: Update README

# on:
#   push:
#     paths:
#       - 'gpts/**'

# jobs:
#   update-readme:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v2
#       - name: Find the most recently committed file in the gpts directory
#         id: findfile
#         run: |
#           # Get the names of files changed in the most recent commit affecting the 'gpts/' directory
#           echo "Fetching the most recent file changes in 'gpts/' directory..."
#           CHANGED_FILES=$(git log -n 1 --pretty="" --name-only -- 'gpts/')

#           echo "Changed files in the most recent commit:"
#           echo "$CHANGED_FILES"

#           # Check if CHANGED_FILES is empty
#           if [[ -z "$CHANGED_FILES" ]]; then
#             echo "No files changed in the most recent commit in 'gpts/' directory."
#             exit 0
#           fi

#           # Selecting the first file from the list of changed files
#           NEW_FILE=$(echo "$CHANGED_FILES" | head -n 1)
#           echo "Most recently committed file in 'gpts/': $NEW_FILE"

#           if [[ ! -z "$NEW_FILE" ]]; then
#             echo "NEW_FILE=$NEW_FILE" >> $GITHUB_ENV
#           fi

#       - name: Print new file content (for debugging)
#         if: env.NEW_FILE
#         run: |
#           NEW_FILE=${{ env.NEW_FILE }}
#           echo "Contents of $NEW_FILE:"
#           cat "$NEW_FILE"

#       - name: Update README
#         if: env.NEW_FILE
#         run: |
#           NEW_FILE=${{ env.NEW_FILE }}
#           CONTENT=$(cat "$NEW_FILE")
#           printf "\n\n - $CONTENT" >> README.md
#           git config --local user.email "action@github.com"
#           git config --local user.name "GitHub Action"
#           git add README.md
#           git commit -m "Update README with new content from $NEW_FILE"
#           git push
