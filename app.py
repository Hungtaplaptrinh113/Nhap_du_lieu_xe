import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime


EXCEL_FILE = "du_lieu_sua_chua.xlsx"


def load_existing_data(path: Path) -> pd.DataFrame:
    if path.exists():
        try:
            return pd.read_excel(path)
        except Exception:
            # Nếu file lỗi định dạng, trả về DataFrame rỗng
            return pd.DataFrame()
    return pd.DataFrame()


def append_to_excel(path: Path, new_row: dict) -> None:
    df_existing = load_existing_data(path)
    df_new = pd.DataFrame([new_row])

    if df_existing.empty:
        df_result = df_new
    else:
        df_result = pd.concat([df_existing, df_new], ignore_index=True)

    # Ghi lại toàn bộ file để tránh lỗi mode append trên một số hệ thống
    df_result.to_excel(path, index=False)


def main():
    st.set_page_config(
        page_title="Nhập thông tin sửa chữa xe",
        page_icon="🛠",
        layout="centered",
    )

    st.title("Nhập thông tin sửa chữa xe")
    st.write("Nhập thông tin bên dưới, dữ liệu sẽ được lưu vào file Excel.")

    excel_path = Path(EXCEL_FILE)

    with st.form("form_sua_chua"):
        col1, col2 = st.columns(2)

        with col1:
            ten_khach = st.text_input("Tên khách hàng")
            so_dien_thoai = st.text_input("Số điện thoại")
            bien_so = st.text_input("Biển số xe")

        with col2:
            hieu_xe = st.text_input("Hiệu xe / Model")
            ngay_nhan = st.date_input(
                "Ngày nhận xe",
                value=datetime.today(),
                format="DD/MM/YYYY",
            )
            chi_phi_du_kien = st.number_input(
                "Chi phí dự kiến (VNĐ)", min_value=0.0, step=100000.0
            )

        mo_ta_hu_hong = st.text_area("Mô tả hư hỏng / Yêu cầu sửa chữa", height=120)

        submitted = st.form_submit_button("Lưu vào Excel")

        if submitted:
            if not ten_khach or not bien_so:
                st.error("Vui lòng nhập tối thiểu 'Tên khách hàng' và 'Biển số xe'.")
            else:
                new_row = {
                    "Thời gian lưu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Tên khách hàng": ten_khach,
                    "Số điện thoại": so_dien_thoai,
                    "Biển số xe": bien_so,
                    "Hiệu xe": hieu_xe,
                    "Ngày nhận xe": ngay_nhan.strftime("%Y-%m-%d"),
                    "Mô tả hư hỏng": mo_ta_hu_hong,
                    "Chi phí dự kiến": chi_phi_du_kien,
                }

                try:
                    append_to_excel(excel_path, new_row)
                    st.success(f"Đã lưu thông tin vào file '{EXCEL_FILE}'.")
                except Exception as e:
                    st.error(f"Không thể ghi vào file Excel: {e}")

    st.markdown("---")
    st.subheader("Dữ liệu đã lưu")

    df = load_existing_data(excel_path)
    if df.empty:
        st.info("Chưa có dữ liệu nào trong file Excel.")
    else:
        st.dataframe(df)

        with open(excel_path, "rb") as f:
            st.download_button(
                label="Tải file Excel",
                data=f,
                file_name=EXCEL_FILE,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )


if __name__ == "__main__":
    main()

