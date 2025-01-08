import redis

try:
    # Redis 연결
    r = redis.Redis(
        host='hanslab.org',
        port=56379,
        charset='utf-8',
        decode_responses=True
    )

    # Redis 서버 정보 조회
    info = r.info()
    print("Redis 서버 정보:")
    print(info)
except Exception as e:
    print(f"Redis 서버 연결 실패: {e}")