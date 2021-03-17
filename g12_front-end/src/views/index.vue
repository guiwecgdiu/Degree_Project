<template>
    <div>
        <div class="home-header">
            <div class="home-header-nav">
                <div class="block_logo"></div>
                <div class="block_nav">
                    <el-menu
                            class="home-nav"
                            mode="horizontal"
                            @select="handleSelect"
                            background-color="#545c64"
                            text-color="#fff"
                            active-text-color="#ffd04b">
                        <el-menu-item index="1" style="background: rgba(84, 92, 100, 0.5);">login</el-menu-item>
                        <el-menu-item index="2" style="background: rgba(84, 92, 100, 0.5);">register</el-menu-item>
                    </el-menu>
                </div>
            </div>
            <div class="home-header-content">
                <P class="p-header-content">Find your favorite house</P>
                <el-input
                    placeholder="Please input the house name, location, house type and other characteristics"
                    suffix-icon="el-icon-search"
                    v-model="searchValue"
                    class="input_search"
                >
                </el-input>
            </div>
        </div>
        <div class="home-main">
            <div class="recommendation-carousel">
                <p class="recommendation-title">Recommended housing</p>
                <el-carousel :interval="4000" type="card" height="300px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >
<!--                        <h3 class="medium" :style="{backgroundImage: item.image}">{{ item.name }}</h3>-->
                        <div  style="position: relative;width: 100%;height: 100%">
                            <el-image
                                    src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                                    fit="cover"
                                    style="width: 100%;height: 100%"
                            >
                            </el-image>
                            <p style="position: absolute;left: 10px;bottom: 0px;font-size: 1.5rem;background: rgba(84, 92, 100, 0.5);width: 100%;text-align: left;padding-left: 5%;color: white">{{item.name}}</p>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="recommendation-carousel">
                <p class="recommendation-title">latest housing</p>
                <el-carousel :interval="4000" type="card" height="300px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >
                        <!--                        <h3 class="medium" :style="{backgroundImage: item.image}">{{ item.name }}</h3>-->
                        <div  style="position: relative;width: 100%;height: 100%">
                            <el-image
                                    src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                                    fit="cover"
                                    style="width: 100%;height: 100%"
                            >
                            </el-image>
                            <p style="position: absolute;left: 10px;bottom: 0px;font-size: 1.5rem;background: rgba(84, 92, 100, 0.5);width: 100%;text-align: left;padding-left: 5%;color: white">{{item.name}}</p>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        props: {
            msg: String,
        },
        data() {
            return {
                searchValue: "",
                activeIndex:0,
                recommendationList:[{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"}]
            }
        }
    }
</script>

<style scoped>
    .home-header{
        width: 100%;
        height: 600px;
        background-image: url("https://s1.ljcdn.com/feroot/pc/asset/img/home/bannerV2.jpg");
        background-position: center;
        background-repeat:no-repeat;
        background-origin:content-box;
        background-size: cover;
        margin-bottom: 20px;
    }
    .home-header-nav{
        width: 100%;
        height: 50px;
    }
    .home-header-content{
        width: 100%;
        height: calc(100% - 50px);
    }
    .home-header-content .input_search{
        width: 60%;
        margin: 40px auto 0 auto;
    }
    .home-header-content .p-header-content{
        text-align: center;
        margin: 150px auto 0 auto;
        color: white;
        font-size: 2rem;
    }
    .block_nav{
        display: flex;
        flex-direction: row-reverse;
        background: rgba(84, 92, 100, 0.5);
    }
    .home-main{
        width: 100%;
    }
    .home-main .recommendation-carousel{
        width: 100%;
        padding: 10px 0;
    }
    .recommendation-carousel .recommendation-title{
        font-size: 1.8rem;
        color: white;
    }

</style>
<style>
    .block_nav ul{
        background: transparent!important;
    }
    .block_nav li{
        background: transparent!important;
    }
</style>
