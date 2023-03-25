# dserve
Deep learning models SERVing with Python
We run `gunicorn` with `uvicorn` workers and served by `FastAPI` api.

## How it works
The gunicorn configuration is automatically loaded from `src/gunicorn_conf.py`, while server startup script is located at `src/gunicorn.sh`. Memory is shared between processes so the models are loaded in ram before the fork of the gunicorn workers.

## Build
```
docker build -f Dockerfile -t dserve .
```

## Run
```
docker run -p 8080:8080 -it --rm dserve
```

## Debug
```
docker run -it --rm dserve bash
gunicorn --chdir /app api:app -w 4 --preload -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py
```

## Test
To test parallelism run model inference calls in parallel. Set `w` as number of calls number to spawn.
```
w=10; seq $w | parallel -j$w curl --silent -G -d 'q=hello%20how%20are%20you' http://localhost:8080/predict/langid
 ```

 Need `parallel` and `curl`:
 - linux: apt-get install curl parallel
 - macos: brew install curl parallel

## Tree
```
.
├── Dockerfile
├── LICENSE
├── README.md
└── src
    ├── api.py
    ├── gunicorn.sh
    ├── gunicorn_conf.py
    ├── models
    │   └── fasttext
    │       └── lid.176.ftz
    ├── models.py
    ├── requirements-dl.txt
    ├── requirements.txt
    └── util.py

3 directories, 11 files
```

## Docs
- FastAPI, https://fastapi.tiangolo.com/
- FastAPI, Serving ML models with multiple workers linearly adds the RAM's load https://github.com/tiangolo/fastapi/issues/2425#issuecomment-734790381
- uvicorn running with gunicorn, https://www.uvicorn.org/#running-with-gunicorn
- gunicorn, https://docs.gunicorn.org/en/latest/index.html

## Disclaimer
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.