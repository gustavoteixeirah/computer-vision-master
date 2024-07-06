import os


if __name__ == '__main__':
    os.system('uvicorn app:app --reload --port 5000')

# import uvicorn
#
# if name == "__main__":
#
# uvicorn.run(
#
#     "app:app",
#
#     host="localhost",
#
#     port=8000,
#
#     reload=True,
#
# )