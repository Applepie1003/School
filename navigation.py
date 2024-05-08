def dijkstra(graph, start, end):
    # 시작 정점으로부터의 거리를 저장하는 딕셔너리
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # 시작 정점의 거리는 0

    # 방문한 정점들을 기록하는 집합
    visited = set()

    while len(visited) < len(graph):
        # 아직 방문하지 않은 정점들 중에서 가장 가까운 정점을 찾음
        current_vertex = min((vertex for vertex in graph if vertex not in visited), key=lambda x: distances[x])

        # 현재 정점을 방문한 것으로 표시
        visited.add(current_vertex)

        # 현재 정점의 이웃 정점들을 반복
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # 만약 현재 정점을 거쳐서 이웃 정점까지의 거리가 더 짧으면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances[end]

# 그래프를 딕셔너리로 표현
graph = {
    # 1호선
    '서울역': {'시청': 120},
    '시청': {'종각': 120, '서울역': 120},
    '종각': {'종로3가': 90, '시청': 120},
    '종로3가': {'종로5가': 90, '종각': 90},
    '종로5가': {'동대문': 90, '종로3가': 90},
    '동대문': {'동묘앞': 60, '종로5가': 90},
    '동묘앞': {'신설동': 90, '동대문': 60},
    '신설동': {'제기동': 90, '동묘앞': 90},
    '제기동': {'청량리': 90, '신설동': 90},
    '청량리': {'제기동': 90},
    # 2호선
    '시청': {'을지로입구': 90},
    '을지로입구': {'을지로3가': 60, '시청': 90},
    '을지로3가': {'을지로4가': 60, '을지로입구': 60},
    '을지로4가': {'동대문역사문화공원': 60, '을지로3가': 60},
    '동대문역사문화공원': {'신당': 90, '을지로4가': 60},
    '신당': {'상왕십리': 60, '동대문역사문화공원': 90},
    '상왕십리': {'왕십리': 60, '신당': 60},
    '왕십리': {'한양대': 60, '상왕십리': 60},
    '한양대': {'뚝섬': 90, '왕십리': 60},
    '뚝섬': {'성수': 90, '한양대': 90},
    '성수': {'건대입구': 60, '뚝섬': 90},
    '건대입구': {'구의': 90, '성수': 60},
    '구의': {'강변': 120, '건대입구': 90},
    '강변': {'잠실나루': 60, '구의': 120},
    '잠실나루': {'잠실': 120, '강변': 60},
    '잠실': {'잠실새내': 60, '잠실나루': 120},
    '잠실새내': {'종합운동장': 90, '잠실': 60},
    '종합운동장': {'삼성': 90, '잠실새내': 90},
    '삼성': {'선릉': 60, '종합운동장': 90},
    '선릉': {'역삼': 60, '삼성': 60},
    '역삼': {'강남': 90, '선릉': 60},
    '강남': {'교대': 60, '역삼': 90},
    '교대': {'서초': 90, '강남': 60},
    '서초': {'방배': 120, '교대': 90},
    '방배': {'사당': 120, '서초': 120},
    '사당': {'낙성대': 120, '방배': 120},
    '낙성대': {'서울대입구': 60, '사당': 120},
    '서울대입구': {'봉천': 90, '낙성대': 60},
    '봉천': {'신림': 60, '서울대입구': 90},
    '신림': {'신대방': 120, '봉천': 60},
    '신대방': {'구로디지털단지': 90, '신림': 120},
    '구로디지털단지': {'대림': 90, '신대방': 90},
    '대림': {'신도림': 90, '구로디지털단지': 90},
    '신도림': {'문래': 120, '대림': 90},
    '문래': {'영등포구청': 120, '신도림': 120},
    '영등포구청': {'당산': 60, '문래': 120},
    '당산': {'합정': 90, '영등포구청': 60},
    '합정': {'홍대입구': 150, '당산': 90},
    '홍대입구': {'신촌': 90, '합정': 150},
    '신촌': {'이대': 60, '홍대입구': 90},
    '이대': {'아현': 60, '신촌': 60},
    '아현': {'충정로': 90, '이대': 60},
    '충정로': {'시청': 90, '아현': 90},
    '용답': {'신답': 90},
    '신답': {'용답': 90, '용두': 90},
    '용두': {'신설동': 90, '신답': 90},
    '신설동': {'용두': 90, '도림천': 90},
    '도림천': {'신설동': 90, '양천구청': 90},
    '양천구청': {'도림천': 90, '신정네거리': 150},
    '신정네거리': {'양천구청': 150, '까치산': 90},
    '까치산': {'신정네거리': 90},
    # 3호선
    '지축': {'구파발': 180},
    '구파발': {'연신내': 180, '지축': 180},
    '연신내': {'불광': 120, '구파발': 180},
    '불광': {'녹번': 90, '연신내': 120},
    '녹번': {'홍제': 90, '불광': 90},
    '홍제': {'무악재': 120, '녹번': 90},
    '무악재': {'독립문': 90, '홍제': 120},
    '독립문': {'경복궁': 90, '무악재': 90},
    '경복궁': {'안국': 120, '독립문': 90},
    '안국': {'종로3가': 90, '경복궁': 120},
    '종로3가': {'을지로3가': 60, '안국': 90},
    '을지로3가': {'충무로': 60, '종로3가': 60},
    '충무로': {'동대입구': 90, '을지로3가': 60},
    '동대입구': {'약수': 90, '충무로': 90},
    '약수': {'금호': 60, '동대입구': 90},
    '금호': {'옥수': 60, '약수': 60},
    '옥수': {'압구정': 60, '금호': 60},
    '압구정': {'신사': 120, '옥수': 60},
    '신사': {'잠원': 120, '압구정': 120},
    '잠원': {'고속터미널': 90, '신사': 120},
    '고속터미널': {'교대': 90, '잠원': 90},
    '교대': {'남부터미널': 120, '고속터미널': 90},
    '남부터미널': {'양재': 90, '교대': 120},
    '양재': {'매봉': 120, '남부터미널': 90},
    '매봉': {'도곡': 120, '양재': 120},
    '도곡': {'대치': 90, '매봉': 120},
    '대치': {'학여울': 60, '도곡': 90},
    '학여울': {'대청': 60, '대치': 60},
    '대청': {'일원': 90, '학여울': 60},
    '일원': {'수서': 90, '대청': 90},
    '수서': {'가락시장': 120, '일원': 90},
    '가락시장': {'경찰병원': 120, '수서': 120},
    '경찰병원': {'오금': 60, '가락시장': 120},
    '오금': {'경찰병원': 60},
    # 4호선
    '당고개': {'상계': 90},
    '상계': {'노원': 90, '당고개': 90},
    '노원': {'창동': 120, '상계': 90},
    '창동': {'쌍문': 120, '노원': 120},
    '쌍문': {'수유': 90, '창동': 120},
    '수유': {'미아': 120, '쌍문': 90},
    '미아': {'미아사거리': 90, '수유': 120},
    '미아사거리': {'길음': 120, '미아': 90},
    '길음': {'성신여대입구': 120, '미아사거리': 120},
    '성신여대입구': {'한성대입구': 120, '길음': 120},
    '한성대입구': {'혜화': 90, '성신여대입구': 120},
    '혜화': {'동대문': 90, '한성대입구': 90},
    '동대문': {'동대문역사문화공원': 90, '혜화': 90},
    '동대문역사문화공원': {'충무로': 60, '동대문': 90},
    '충무로': {'명동': 60, '동대문역사문화공원': 60},
    '명동': {'회현': 60, '충무로': 60},
    '회현': {'서울역': 60, '명동': 60},
    '서울역': {'숙대입구': 90, '회현': 60},
    '숙대입구': {'삼각지': 90, '서울역': 90},
    '삼각지': {'신용산': 90, '숙대입구': 90},
    '신용산': {'이촌': 60, '삼각지': 90},
    '이촌': {'동작': 90, '신용산': 60},
    '동작': {'총신대입구': 180, '이촌': 90},
    '총신대입구': {'사당': 90, '동작': 180},
    '사당': {'남태령': 90, '총신대입구': 90},
    '남태령': {'사당': 90}
}

start_vertex = input("시작 정점을 입력하세요: ")
end_vertex = input("종착 정점을 입력하세요: ")

shortest_distance = dijkstra(graph, start_vertex, end_vertex)

print(f"{start_vertex} 에서 {end_vertex} 까지의 최단 거리:", shortest_distance)
