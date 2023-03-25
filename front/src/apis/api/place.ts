import { defaultInstance } from "../utils";

// GET APIs

/**
 * GET : 시/도 리스트 데이터를 가져온다.
 * @returns  [] : 시/도 id, 시/도 name을 가진 Item 배열
 */
export const getSidoList = async () => {
  const { data } = await defaultInstance.get("sido");
  return data;
};

/**
 * @param {string} sido : 시/도 코드
 * GET : 구/군 리스트 데이터를 가져온다.
 * @returns  [] : 구/군 id, 구/군 name을 가진 Item 배열
 */
export const getGugunList = async (sido: string) => {
  const { data } = await defaultInstance.get(`gugun/${sido}`);
  return data;
};

/**
 * @param {string} word : 검색어
 * GET : 검색어의 낱말을 포함한 가게 정보를 나열한다.
 * @returns {PlaceholderInSubject, name, thumbNailUrl}
 */
export const getListWithSearchWord = async (searchWord: string) => {
  const { data } = await defaultInstance.get(`places/auto/${searchWord}`);
  return data;
};

/**
 * @param {number} userSeq : 사용자번호
 * @param {number} placeId : 장소 ID
 * @param {string} type: 장소 유형
 * GET : 장소의 상세 정보를 가져온다.
 * @returns {장소 type마다 다름}
 */
export const getPlaceDetail = async (
  userSeq: number,
  placeId: number,
  type: string
) => {
  const { data } = await defaultInstance.get(
    `places/detail/users/${userSeq}/placeId/${placeId}/type/${type}`
  );
  return data;
};