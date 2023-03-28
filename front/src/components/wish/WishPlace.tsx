import { Star } from "@mui/icons-material";
import { Icon } from "@iconify/react";
import Swal from "sweetalert2";
import { getWishPlaceList } from "../../apis/api/wish";
import { useQuery } from "react-query";
import { useRecoilState } from "recoil";
import { userState } from "../../recoil/states/UserState";

/* eslint-disable jsx-a11y/alt-text */
type propsType = {
    id: number;
    title: string;
    address: string;
    content: string;
    star: number;
    heart: boolean;
};

export default function WishPlace() {
    const userSeq = useRecoilState(userState);
    // const { data, isLoading } = useQuery({
    //     queryKey: ["getWishPlaceList", "userSeq"],
    //     queryFn: () => getWishPlaceList(userSeq[0].seq),
    // });

    let list: propsType[] = [
        {
            id: 0,
            title: "사발",
            address: "서울 종로구 사직로8길 34 경희궁의아침 3단지 사발 142호",
            content:
                "서울 광화문에 위치한 사발은 새로운 스타일의 퓨전국수, 덮밥, 국밥을 정성스롭고 아름답게 대접합니다.",
            star: 4.5,
            heart: true,
        },
        {
            id: 1,
            title: "후라토식당 경복궁 본점",
            address: "서울 종로구 자하문로7길 11",
            content: "숙성사시미 전문 캐쥬얼 스시야",
            star: 3.5,
            heart: true,
        },
        {
            id: 2,
            title: "해운대 우시야",
            address: "부산 해운대구 우동1로38번길 2",
            content: "부산 소고기 오마카세 수요미식회에도 나온 맛있는 소고기",
            star: 5.0,
            heart: true,
        },
    ];

    return (
        <div>
            <div className="mx-5 mt-5 h-full">
                <div className="title font-medium text-xl inline-block">
                    찜한 장소
                </div>
                <div className="cnt ml-2 font-bold text-red-600 text-xl inline-block">
                    {list.length}
                </div>

                <div className="mt-4 h-[480px] overflow-y-auto">
                    {list.map((a: propsType) => (
                        <Item key={a.id} item={a}></Item>
                    ))}
                </div>

                <div className="w-full h-12 bg-lightMain2 text-white font-bold text-center text-xl pt-2.5 mt-3 rounded-full">
                    찜한 장소로 코스 만들기
                </div>
            </div>
        </div>
    );
}

function Item(props: { item: propsType }) {
    let address =
        props.item.address.length > 18
            ? props.item.address.slice(0, 18).concat("...")
            : props.item.address;
    let content =
        props.item.content.length > 30
            ? props.item.content.slice(0, 30).concat("...")
            : props.item.content;

    return (
        <div className="col-md-4 mb-4 p-3 h-40 bg-calendarGray rounded-lg">
            <div className="heart mb-2 float-right">
                {props.item.heart && (
                    <Icon
                        icon="mdi:cards-heart"
                        color="#ff8e9e"
                        width="28"
                        height="28"
                        onClick={() => {
                            Swal.fire({
                                // title: `${props.item.title}을 찜 해제하시겠습니까?`,
                                text: `${props.item.title}을(를) 찜 해제하시겠습니까?`,
                                icon: "question",

                                showCancelButton: true, // cancel버튼 보이기. 기본은 원래 없음
                                confirmButtonColor: "#FF8E9E", // confrim 버튼 색깔 지정
                                cancelButtonColor: "#B9B9B9", // cancel 버튼 색깔 지정
                                confirmButtonText: "승인", // confirm 버튼 텍스트 지정
                                cancelButtonText: "취소", // cancel 버튼 텍스트 지정
                            }).then((result) => {
                                // 만약 Promise리턴을 받으면,
                                if (result.isConfirmed) {
                                    // 만약 모달창에서 confirm 버튼을 눌렀다면
                                    // 해당 장소 찜 목록에서 삭제
                                    const Toast = Swal.mixin({
                                        toast: true, // 토스트 형식
                                        position: "bottom-end", // 알림 위치
                                        showConfirmButton: false, // 확인버튼 생성 유무
                                        timer: 1000, // 지속 시간
                                        timerProgressBar: true, // 지속시간바 생성 여부
                                    });

                                    Toast.fire({
                                        icon: "success",
                                        title: "삭제되었습니다. ",
                                    });
                                }
                            });
                        }}
                    />
                )}
                {!props.item.heart && (
                    <Icon
                        icon="mdi:cards-heart-outline"
                        color="#ff8e9e"
                        width="28"
                        height="28"
                    />
                )}
            </div>

            <div className="font-bold mb-2">{props.item.title}</div>

            <img
                className="float-left w-24 h-[100px] mr-2 rounded-md"
                src="https://img.siksinhot.com/place/1600741858600366.jpg?w=307&h=300&c=Y"
            />

            <div className="star ml-2 mb-1">
                <Star fontSize="small" sx={{ color: "#FF8E9E" }} />
                <p className="inline-block text-sm ml-1 text-lightMain">
                    {props.item.star}
                </p>
            </div>
            <div className="mb-2 text-sm text-gray-500">{address}</div>
            <div className="text-sm">{content}</div>
        </div>
    );
}